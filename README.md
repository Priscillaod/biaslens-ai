# BiasLens AI

**BiasLens AI** is an Azure-powered platform that helps healthcare professionals, administrators, and researchers detect bias in clinical notes, patient feedback, and medical documentation.  
By analyzing unstructured text for subtle but harmful language related to gender, race, age, and ability, it brings responsible AI and equity into the heart of healthcare systems.

##  Hackathon Challenge: Handling Unstructured Data

### NLP-Powered Bias Detection
- Uses Azure OpenAI to identify problematic phrases like "non-compliant", "emotional", or "aggressive"
- Context-aware flagging and suggestions for inclusive rewrites

### Empowering Healthcare Professionals
- Streamlit app interface for real-time analysis
- Inclusive nudges during documentation
- Supports training and reflection modules

### Responsible and Ethical AI
- SHAP/LIME for optional explainability
- Azure Content Safety integration
- Anonymized NLP processing for compliance

### Use Case Example (Trauma & Orthopaedics)
**Input:** "Patient appears overly emotional and uncooperative. History unclear."  
**Output:** Flags "overly emotional" as gender-coded and "uncooperative" as ambiguous.  
**Suggested Rewrite:** "Patient expressed distress during session; full history not yet confirmed."

## Key Features
- Bias Detection Engine
- Explainable Language Insights
- Inclusive Suggestions
- Streamlit UI
- Bias Reporting (Coming Soon)

## Goals
- Reduce unconscious bias in healthcare documentation
- Improve accuracy and inclusivity in clinical notes
- Promote responsible and explainable AI in healthcare

## Tech Stack
- Azure OpenAI
- Streamlit
- Azure Content Safety
- Python
- SHAP / LIME (Optional)
- Azure Blob Storage
- Azure Static Web Apps

## Social Impact
BiasLens AI promotes SDGs:
- **3** Good Health & Wellbeing
- **5** Gender Equality
- **10** Reduced Inequalities

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Priscillaod/biaslens-ai.git
cd biaslens-ai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI key
Create a `.env` file:
```
OPENAI_API_KEY=your-key-here
```

### 4. Run locally
```bash
streamlit run app/main.py
```

---

Built for the Microsoft Innovation Hackathon 2025.