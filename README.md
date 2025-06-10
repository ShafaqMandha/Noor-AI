# Noor.AI

Noor.AI is an AI-powered skincare assistant project designed to provide personalized beauty advice, analyse skin types, and recommend suitable skincare products. The project is organised into four main modules, each focusing on a specific aspect of the skincare experience.

---

## Project Structure and File Overview

### 1. AI Beauty Advisor  
This module offers personalised beauty advice based on AI analysis. A module combining facial analysis and skincare product recommendation features.

- **AI Beauty Advisor.html** — Frontend interface for the beauty advisor.
- **app.py** — Python backend application that runs the AI logic.
- **cosmetic_p.csv** — Dataset of cosmetic products used by the system.
- **metadata.json** — Model metadata required for AI inference.
- **model.json** — AI model architecture.
- **requirements.txt** — List of Python dependencies needed to run this module.
- **server.py** — Backend server script.
- **weights.bin** — Pre-trained model weights for the AI.

---

### 2. Skin Type Analysis  
This module uses machine learning to classify skin types based on images.

- **AI Skin Analysis.html** — Web interface for uploading user images.
- **metadata.json** — Metadata for the skin classification model.
- **model.json** — Model structure used for skin analysis.
- **weights.bin** — Trained weights of the skin classification model.
- **Skin Types Dataset for ML training/** — Image dataset used for training the skin type classifier.
- **Noor.AI – Skin Analysis Feature Development Report.pdf** — Detailed documentation of the skin analysis process, including its design, features, and implementation.

---

### 3. Skincare Product Recommendation  
This module suggests personalized skincare products based on user inputs and preferences.

- **Beauty Matchmaker.html** — Web interface for selecting skincare concerns.
- **app.py** — Backend code that filters and recommends products.
- **cosmetic_p.csv** — Enhanced product dataset with recommendation logic.
- **Noor.AI - Skincare Product Recommendation Feature Development Report.pdf** — Detailed documentation of the skincare product recommendation system's design, features, and implementation.
- **requirements.txt** — Required Python packages to run this recommendation system.

---

### 4. Chatbot  
This module adds a conversational interface to interact with users and provide skincare advice.

- **templates/** — Contains HTML files for the chatbot's user interface.
- **app.py** — Flask backend application handling chatbot logic.
- **.env** — Environment file containing configuration variables (e.g., API keys).
- **cosmetic_p.xlsx** — Skincare product dataset used in chatbot responses.
- **Noor.AI – Skincare Chatbot Feature Development Report.pdf** — Detailed documentation of the chatbot's design, features, and implementation.
- **requirements.txt** — Python dependencies for the chatbot module.

---

## Technologies Used

- Python (Flask, Pandas, NumPy)
- HTML/CSS
- TensorFlow & Teachable Machine
- Google Colab
- Git & GitHub

---

## License

This project is developed for academic and educational use only. Not intended for commercial distribution. 
This project does not replace a dermatologist or a doctor in any way, for skincare advice, always refer to a doctor in advance.
