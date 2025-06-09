from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Load and process the skincare data
def load_skincare_data():
    try:
        df = pd.read_csv('cosmetic_p.csv')
        # Clean column names by stripping whitespace
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def get_dataset_stats(df):
    """Get statistics about the dataset"""
    if df is None or df.empty:
        return {}
    
    try:
        stats = {
            'total_products': len(df),
            'brands': df['brand'].nunique() if 'brand' in df.columns else 0,
            'categories': df['Label'].nunique() if 'Label' in df.columns else 0,
            'avg_rating': round(df['rank'].mean(), 1) if 'rank' in df.columns else 0
        }
        return stats
    except Exception:
        return {}

def get_skincare_context(df):
    """Create a context string from the skincare data"""
    if df is None or df.empty:
        return "No data available."
        
    try:
        context = """You are a skincare assistant that MUST ONLY provide recommendations and information based on the following dataset. 
        DO NOT make recommendations about products that are not in this dataset.
        DO NOT provide general skincare advice without referencing specific products from the dataset.
        
        Dataset Overview:
        """
        
        # Add general statistics
        context += f"Total number of products: {len(df)}\n"
        context += f"Product categories: {', '.join(df['Label'].dropna().unique())}\n"
        context += f"Brands available: {', '.join(df['brand'].dropna().unique())}\n\n"
        
        # Add detailed product information (limit to first 10 products to avoid context length issues)
        context += "Available Products (showing first 10):\n"
        for _, row in df.head(10).iterrows():
            try:
                context += f"Product: {row['brand']} {row['name']}\n"
                context += f"Category: {row['Label']}\n"
                context += f"Price: ${row['price']}\n"
                context += f"Rating: {row['rank']}\n"
                context += f"Ingredients: {row['ingredients']}\n"
                context += "Suitable for skin types: "
                skin_types = []
                if row.get('Combination'): skin_types.append('Combination')
                if row.get('Dry'): skin_types.append('Dry')
                if row.get('Normal'): skin_types.append('Normal')
                if row.get('Oily'): skin_types.append('Oily')
                if row.get('Sensitive'): skin_types.append('Sensitive')
                context += ', '.join(skin_types) + "\n"
                context += f"Availability: {row.get('availability', 'Unknown')}\n\n"
            except Exception as e:
                continue
        
        return context
    except Exception as e:
        print(f"Error generating context: {str(e)}")
        return "Error generating context."

def get_chatbot_response(user_input, context, df):
    """Get response from OpenAI API"""
    if df is None or df.empty:
        return "I apologize, but I'm currently unable to access the product database. Please try again later."
        
    try:
        messages = [
            {"role": "system", "content": f"""You are Noor, a skincare assistant that provides personalized skincare recommendations.
            
{context}

STRICT GUIDELINES:
1. ONLY recommend products that are available in our collection
2. When suggesting products, use this conversational format:
   "I can recommend [product name] by [brand] for [price] - Available at: [availability information]
   This [product type] contains ingredients like [key ingredients], which is beneficial for [skin type]:
   * Primary benefit: [main benefit]
   * Secondary benefits: [additional benefits]"

3. For ingredient questions:
   - Provide scientifically-backed benefits of ingredients
   - Include specific examples of products that contain these ingredients
   - Format ingredient benefits as follows:
     * Primary benefit: [main benefit]
     * Secondary benefits: [additional benefits]
     * How it works: [brief scientific explanation]
     * Products containing this ingredient: [list relevant products]
   - Only discuss ingredients that are present in our products
   - Be precise and accurate about ingredient benefits
   - Avoid making unsubstantiated claims
   - If an ingredient's benefits are not well-documented, acknowledge this limitation

4. For routine building:
   - Only suggest products from our collection
   - Consider skin type compatibility
   - Consider product categories (cleanser, moisturizer, etc.)
   - Consider price points
   - Use the same format as above for each product

5. If a user asks about products or ingredients we don't carry:
   - Politely explain that you can only provide information about products we offer
   - Suggest similar products that are available using the format above

6. Keep responses focused on the available products
7. Always verify product availability before recommending

Remember: You can ONLY make recommendations based on the products we offer."""},
            {"role": "user", "content": user_input}
        ]
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=800
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}"

# Load data at startup
df = load_skincare_data()
stats = get_dataset_stats(df)

@app.route('/')
def home():
    return render_template('index.html', stats=stats)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    context = get_skincare_context(df)
    response = get_chatbot_response(user_input, context, df)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 