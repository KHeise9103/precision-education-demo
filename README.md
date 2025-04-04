# 📚 Precision Education Demo App

This is a Streamlit-powered prototype application designed to demonstrate the concept of **precision education** in clinical settings. The app uses simulated patient data and role-based prompt engineering to generate tailored, context-aware learning content.

🧠 **Built for:**  
- Clinicians in acute and inpatient care  
- Educators and informaticists  
- Medical education researchers  
- Partners in the AMA ChangeMedEd Precision Education Initiative  

## 🚀 Features

- 🔍 **Simulated Epic Insights**: Fake patient summaries with realistic clinical data  
- 🧠 **Role-Specific Prompt Generation**: Tailored prompts for Medical Students, Residents, Fellows, APPs, RNs, RTs, and Attendings  
- 📘 **Mock OpenEvidence Output**: Evidence-based guidance summaries based on clinical context  
- 📊 **Learner Metrics Dashboard**: Track what content was requested, by whom, and what feedback was given  

## 🛠 Technology

- [Streamlit](https://streamlit.io/)
- Python 3.11+
- JSON for fake patient scenarios
- Designed for future integration with:
  - Epic Insights (EHR summarization)
  - OpenEvidence (AI literature retrieval)

## 🧪 Try It Out

You can view the deployed app here:  
👉 [Your Streamlit Cloud URL here](https://your-deployed-app.streamlit.app)

Or run it locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run precision_education_demo_with_metrics.py
