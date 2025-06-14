# 🌸 Noor.AI – AI-Powered Skincare Assistant

**Noor.AI** is an AI-powered skincare assistant designed to deliver personalised beauty advice through facial analysis, skin type classification, product recommendation, and chatbot support. This project combines machine learning, web development, and user experience design into one seamless skincare solution.

> ⚠️ *This application is for academic and educational use only. It is not a substitute for professional medical or dermatological advice.*

---

## 🌐 Live Demo & Feedback

🔗 **Access the application here:** [Noor.AI Web App](https://noor-ai.onrender.com)  
📝 **Share your thoughts:** [Feedback Form](https://forms.gle/Pvqz7QMMYAD6cUSi6)

---

## 🚀 Deployment Overview

📁 **`Noor_AI_Deployment_Files`**  
This folder contains all finalised, cleaned, and structured files used during the deployment process.  
It follows a consistent structure inspired by the **AI Beauty Advisor** module and integrates all key components (backend, models, UI, and assets) in a format ready for hosting or deployment.

In order to deploy the project on [Render](https://render.com), I had to commit the finalised and cleaned deployment-ready files to a **separate new repository**. This ensured a lightweight, organised structure optimised for hosting, with only the essential components needed for running the application. The same code files are saved under the **`Noor_AI_Deployment_Files`** folder 


---

## ✅ Testing & Development Process

Before preparing for deployment, each module was **individually developed and tested** to ensure proper functionality:

1. **Individual Testing Phase**  
   Each core component—**AI Beauty Advisor**, **Skin Type Analysis**, **Product Recommendation**, and **Chatbot**—was tested as a standalone feature.  
   - ✅ Facial analysis was tested for accuracy using local model predictions  
   - ✅ Skin type classification was trained and tested using a dataset in Google Colab  
   - ✅ Product recommendation logic was tested with various user inputs  
   - ✅ Chatbot functionality and response flow were tested with dynamic queries  

   📄 *Detailed documentation for each component is available in its respective folder.*

2. **Integration Phase**  
   Once individual testing was complete, modules were combined to test:
   - Inter-module compatibility
   - Data flow across features (e.g., using skin type in product filtering)
   - Interface consistency

3. **Deployment File Preparation**  
   The final deployment-ready files were organized into `Noor_AI_Deployment_Files`, maintaining a clean structure for easy hosting or presentation.

---

## 📁 Project Structure

### 1. `Noor_AI_Deployment_Files`  
- Final deployment build with:
  - UI files (HTML/CSS)
  - `app.py` (Flask backend)
  - ML model files: `model.json`, `weights.bin`, `metadata.json`
  - Datasets used: `cosmetic_p.csv` and others
  - `requirements.txt` for environment setup

---

### 2. AI Beauty Advisor  
Provides personalised skincare suggestions based on facial analysis.

**Key Files:**
- `AI Beauty Advisor.html` – Frontend interface  
- `app.py`, `server.py` – Backend logic  
- Pre-trained ML files (`model.json`, `weights.bin`)  
- `cosmetic_p.csv` – Skincare product dataset  
- 📄 `Noor.AI – Beauty Advisor Feature Development Report.pdf`

---

### 3. Skin Type Analysis  
Classifies user skin type using ML models trained on image data.

**Key Files:**
- `AI Skin Analysis.html` – Upload-based interface  
- Trained model files  
- `Skin Types Dataset for ML training/`  
- 📄 `Noor.AI – Skin Analysis Feature Development Report.pdf`

---

### 4. Skincare Product Recommendation  
Filters and recommends skincare products based on user needs.

**Key Files:**
- `Beauty Matchmaker.html` – User input interface  
- `app.py` – Recommendation logic  
- `cosmetic_p.csv` – Enhanced dataset  
- 📄 `Noor.AI - Skincare Product Recommendation Feature Development Report.pdf`

---

### 5. Chatbot  
Conversational interface for skincare advice.

**Key Files:**
- `templates/` – HTML interface for the chatbot  
- `app.py` – Chatbot backend (Flask)  
- `.env` – API key management  
- `cosmetic_p.xlsx` – Dataset for chatbot responses  
- 📄 `Noor.AI – Skincare Chatbot Feature Development Report.pdf`

---

## 💻 Technologies Used

- **Languages/Frameworks:** Python (Flask), HTML, CSS  
- **ML/AI Tools:** TensorFlow, Teachable Machine, Google Colab  
- **Libraries:** Pandas, NumPy  
- **Tools:** GitHub, VS Code

---

## 📌 Notes

- This project is optimised for use on desktop or tablet devices.  
- Some features (e.g., chatbot and facial analysis) require an active internet connection and may use external APIs or model libraries.  
- Make sure `.env` is configured properly before running the chatbot.

---

## 📄 License & Disclaimer

- **License:** Educational Use Only  
- **Disclaimer:** Noor.AI is not intended to diagnose or treat any skin condition. Always consult with a licensed dermatologist for skin-related concerns.
