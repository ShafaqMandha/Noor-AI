from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

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
    filtered = df[(df[skin_type] == 1) | (df["skin_type_coverage"] >= 2)]
    if budget:
        filtered = filtered[filtered["price"] <= budget]
    filtered_sorted = filtered.sort_values(by=["Label", "rank"], ascending=[True, False])
    recommendations = filtered_sorted.groupby("Label").head(top_n_per_type)
    return recommendations[["Label", "brand", "name", "price", "rank"]]

# Route
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
    html = open("Beauty Matchmaker.html", encoding="utf-8").read()
    return render_template_string(html, table=recommendations.to_html(classes='table table-striped', index=False) if recommendations is not None else None, error=error)

if __name__ == '__main__':
    app.run(debug=True)
