
import streamlit as st
import json
from pathlib import Path
from datetime import datetime

# Load fake patient data from JSON
DATA_PATH = Path(__file__).parent / "fake_patients.json"
with open(DATA_PATH, "r") as f:
    patients = json.load(f)

# In-memory tracking of session interactions
if "interaction_log" not in st.session_state:
    st.session_state.interaction_log = []

# Enhanced prompt generation logic
def generate_prompt(patient_data, role):
    active_problems = patient_data.get("active_problems", [])
    prompt = ""

    if "Sepsis" in active_problems:
        prompt += "Summarize current guideline-based management of sepsis, including initial resuscitation, antibiotic timing, and monitoring parameters."
    elif "Chest Pain" in active_problems:
        prompt += "Outline the initial evaluation and treatment of chest pain in the emergency setting, including risk stratification and initial orders."
    elif "Pneumonia" in active_problems:
        prompt += "Summarize inpatient management of community-acquired pneumonia, including diagnostic workup, antimicrobial selection, and monitoring."
    elif "Post-op Day 2 - Colectomy" in active_problems:
        prompt += "Review post-operative care considerations for colectomy, including pain control, wound monitoring, and signs of surgical complications."
    else:
        prompt += "Summarize the appropriate evidence-based management for this patient's current clinical conditions."

    role_addendum = {
        "Medical Student": " Provide definitions and foundational concepts appropriate for a learner in early training.",
        "Resident": " Include diagnostic reasoning and step-by-step clinical decision-making.",
        "Fellow": " Provide nuanced recommendations and incorporate emerging evidence for complex scenarios.",
        "APP": " Emphasize role-specific actions including initiating orders, team communication, and coordination of care.",
        "Attending": " Focus on delegation, oversight, and high-level synthesis of care plans.",
        "RN": " Highlight nursing assessments, monitoring responsibilities, and escalation triggers.",
        "RT": " Detail ventilator strategies, oxygenation goals, and weaning parameters."
    }

    prompt += role_addendum.get(role, " Provide general recommendations suitable for a multidisciplinary care team.")
    return prompt

# Navigation
page = st.sidebar.radio("Navigation", ["🧠 Precision Prompt Demo", "📊 Learner Metrics"])

if page == "🧠 Precision Prompt Demo":
    st.title("📚 Precision Education Demo")
    st.markdown("Prototype platform for delivering real-time educational support using patient context and AI.")

    patient_name = st.selectbox("Select a patient case", list(patients.keys()))
    patient = patients[patient_name]

    role = st.radio("Select your role", ["Medical Student", "Resident", "Fellow", "APP", "Attending", "RN", "RT"])

    st.subheader("🩺 Patient Summary")
    st.write(f"**Location:** {patient['location']}")
    st.write(f"**Age:** {patient['age']}")
    st.write(f"**Active Problems:** {', '.join(patient['active_problems'])}")
    st.write("**Labs:**")
    for lab, value in patient["labs"].items():
        st.write(f"- {lab}: {value}")
    st.write(f"**Recent Orders:** {', '.join(patient['recent_orders'])}")

    st.subheader("🧠 Engineered Prompt")
    engineered_prompt = generate_prompt(patient, role)
    st.code(engineered_prompt)

    st.subheader("📘 OpenEvidence Mock Output")
    if "sepsis" in engineered_prompt.lower():
        st.markdown("""
**Sepsis Management Summary**

- Administer 30 mL/kg IV crystalloids for hypotension or lactate ≥4 mmol/L.
- Give broad-spectrum antibiotics within 1 hour.
- Reassess volume status and perfusion after initial resuscitation.
- Consider vasopressors if MAP < 65 mmHg.

*Source: Surviving Sepsis Campaign 2021*
""")
    elif "chest pain" in engineered_prompt.lower():
        st.markdown("""
**Chest Pain Management Summary**

- Immediate EKG and troponin assessment.
- Administer aspirin.
- Risk stratify based on clinical history and EKG changes.
- Consult cardiology for ongoing ST changes.

*Source: AHA/ACC Guidelines 2020*
""")
    elif "pneumonia" in engineered_prompt.lower():
        st.markdown("""
**Pneumonia Management Summary**

- Obtain chest X-ray and sputum cultures.
- Initiate empiric antibiotics per CAP guidelines.
- Monitor respiratory status and consider escalation of care as needed.

*Source: IDSA/ATS CAP Guidelines 2019*
""")
    else:
        st.markdown("""
**General Management Summary**

- Review condition-specific guidelines.
- Follow institution protocols and reassess regularly.
- Consult specialists as needed.

*Source: Internal Reference*
""")

    st.subheader("🗳️ Feedback")
    feedback = st.radio("Was this helpful?", ["👍 Yes", "👎 No"])
    st.write("Thanks for your feedback!")

    # Log interaction
    st.session_state.interaction_log.append({
        "timestamp": datetime.now().isoformat(),
        "patient": patient_name,
        "role": role,
        "prompt": engineered_prompt,
        "feedback": feedback
    })

elif page == "📊 Learner Metrics":
    st.title("📊 Learner Metrics")
    st.markdown("Session-based view of prompt interactions and learner engagement.")

    if st.session_state.interaction_log:
        for entry in reversed(st.session_state.interaction_log):
            st.markdown(f"""
**{entry['timestamp']}**
- **Patient**: {entry['patient']}
- **Role**: {entry['role']}
- **Feedback**: {entry['feedback']}
- **Prompt**: `{entry['prompt']}`
---
""")
    else:
        st.info("No interactions logged yet. Try using the demo first.")
