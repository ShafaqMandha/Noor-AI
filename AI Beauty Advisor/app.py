from flask import Flask, request, render_template_string, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load and clean the dataset once at startup
df = pd.read_csv("cosmetic_p.csv")

# Clean the data
df["Label"] = df["Label"].str.title().str.strip()
df = df.drop(columns=[col for col in ["Combination", "Sensitive"] if col in df.columns])
skin_cols = ["Dry", "Normal", "Oily"]
df["skin_type_coverage"] = df[skin_cols].sum(axis=1)
label_order = ["Moisturizer", "Cleanser", "Treatment", "Face Mask", "Eye Cream", "Sun Protect"]
df["Label"] = pd.Categorical(df["Label"], categories=label_order, ordered=True)

# Recommendation logic
def recommend_products(skin_type, budget=None, top_n_per_type=2):
    # Products that are suitable for the specific skin type
    skin_type_products = df[df[skin_type] == 1]
    
    # Products that are suitable for all skin types (have high coverage)
    all_skin_products = df[df["skin_type_coverage"] >= 3]  # Products suitable for all 3 skin types
    
    # Combine both sets of products
    filtered = pd.concat([skin_type_products, all_skin_products]).drop_duplicates()
    
    # Apply budget filter if specified
    if budget:
        filtered = filtered[filtered["price"] <= budget]
    
    # Sort by category and rank
    filtered_sorted = filtered.sort_values(by=["Label", "rank"], ascending=[True, False])
    
    # Get top N products per category
    recommendations = filtered_sorted.groupby("Label").head(top_n_per_type)
    
    # Add a flag to indicate if product is suitable for all skin types
    recommendations["is_all_skin"] = recommendations["skin_type_coverage"] >= 3
    
    return recommendations[["Label", "brand", "name", "price", "rank", "Available at", "is_all_skin"]]

# Serve model files
@app.route('/model.json')
def serve_model():
    response = send_from_directory('.', 'model.json')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/metadata.json')
def serve_metadata():
    response = send_from_directory('.', 'metadata.json')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/weights.bin')
def serve_weights():
    response = send_from_directory('.', 'weights.bin')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

# API endpoint for recommendations
@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    skin_type = data.get('skin_type', '').strip()
    
    # Normalize skin type
    skin_type_map = {
        'dry skin': 'Dry',
        'normal skin': 'Normal',
        'oily skin': 'Oily',
        'dry': 'Dry',
        'normal': 'Normal',
        'oily': 'Oily'
    }
    skin_type = skin_type_map.get(skin_type.lower(), skin_type)
    
    if skin_type not in skin_cols:
        return {'error': f'Invalid skin type: {skin_type}. Must be one of: {", ".join(skin_cols)}'}, 400
        
    try:
        budget = data.get('budget')
        recommendations = recommend_products(skin_type, budget)
        
        # Convert recommendations to dict and add a description
        recs_dict = recommendations.to_dict('records')
        for rec in recs_dict:
            if rec['is_all_skin']:
                rec['description'] = f"{rec['Label']} suitable for all skin types"
            else:
                rec['description'] = f"{rec['Label']} for {skin_type} skin"
            # Remove the is_all_skin flag as it's only used internally
            del rec['is_all_skin']
            
        return {'recommendations': recs_dict}
    except Exception as e:
        return {'error': str(e)}, 500

# Main route
@app.route('/', methods=["GET", "POST"])
def index():
    recommendations = None
    error = None

    if request.method == "POST":
        skin_type = request.form.get("skin_type", "").title()
        budget_input = request.form.get("budget", "").strip()

        if skin_type not in skin_cols:
            error = "Invalid skin type selected."
        else:
            try:
                budget = float(budget_input) if budget_input else None
                recommendations = recommend_products(skin_type, budget)
            except Exception as e:
                error = f"Error: {e}"

    # HTML page
    html = open("AI Beauty Advisor.html", encoding="utf-8").read()
    return render_template_string(html, table=recommendations.to_html(classes='table table-striped', index=False) if recommendations is not None else None, error=error)

if __name__ == '__main__':
    print("\nStarting Flask server...")
    print("Available routes:")
    print("1. http://localhost:8000/ - AI Beauty Advisor")
    print("2. http://localhost:8000/model.json - Model file")
    print("3. http://localhost:8000/metadata.json - Model metadata")
    print("4. http://localhost:8000/weights.bin - Model weights")
    print("\nAPI Endpoints:")
    print("- POST http://localhost:8000/api/recommendations - Get product recommendations")
    print("\nPress Ctrl+C to stop the server")
    app.run(debug=True, port=8000)
