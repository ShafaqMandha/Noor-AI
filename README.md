# Noor.AI

Noor.AI is an AI-powered skincare assistant project designed to provide personalized beauty advice, analyze skin types, and recommend suitable skincare products. The project is organized into three main modules, each focusing on a specific aspect of the skincare experience.

---

## Project Structure and File Overview

### 1. AI Beauty Advisor  
This module offers personalized beauty advice based on AI analysis.

- **AI Beauty Advisor.html** — Frontend interface for the beauty advisor.
- **app.py** — Python backend application that runs the AI logic.
- **cosmetic_p.csv** — Dataset of cosmetic products used by the system.
- **metadata.json** — Model metadata required for AI inference.
- **model.json** — AI model architecture.
- **requirements.txt** — List of Python dependencies needed to run this module.
- **weights.bin** — Pre-trained model weights for the AI.

---

### 2. Skin Type Analysis  
This module uses machine learning to classify skin types based on images.

- **AI Skin Analysis.html** — Frontend interface for skin type analysis.
- **metadata.json** — Model metadata.
- **model.json** — AI model architecture.
- **weights.bin** — Pre-trained weights for the skin type classification model.
- **Skin Types Dataset for ML training/** — Folder containing image datasets used to train the model. The dataset was sourced from Kaggle and utilized with Google’s Teachable Machine.

---

### 3. Skincare Product Recommendation  
This module provides personalized skincare product suggestions.

- **app.py** — Python backend application for the recommendation system.
- **Beauty Matchmaker.html** — Frontend interface for product recommendations.
- **cosmetic_p.csv** — Modified dataset of skincare products, including store links. The dataset was initially taken from Kaggle and cleaned using Google Colab to fit the application's purpose.

---

## Additional Information

- The datasets used in this project are mainly sourced from Kaggle and tailored to fit each module’s specific requirements.
- AI models are trained and deployed using TensorFlow and Google Teachable Machine for ease of use and accessibility.
- The project uses Python for backend processing and HTML for user-facing interfaces.

---

Feel free to explore each folder for detailed resources and files used in building this project.

---

If you have any questions or want to contribute, please get in touch!

---

