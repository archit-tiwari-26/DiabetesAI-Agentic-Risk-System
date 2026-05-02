"""
Part 2: Chapters 1-3 content
Run after part1.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from generate_report_part1 import doc, add_heading_styled, add_body, add_bullet, add_centered, page_break, add_table, OUTPUT_PATH

# ══════════════════════════════════════════════════════════════
# CHAPTER 1: INTRODUCTION
# ══════════════════════════════════════════════════════════════
page_break()
add_heading_styled("Chapter 1: Introduction", 1)

add_heading_styled("1.1 Background", 2)
add_body(
    "Type 2 Diabetes Mellitus (T2DM) is a chronic metabolic disorder characterized by insulin "
    "resistance and relative insulin deficiency, resulting in persistent hyperglycemia. According "
    "to the International Diabetes Federation (IDF), approximately 537 million adults aged 20-79 "
    "were living with diabetes in 2021, and this number is projected to rise to 783 million by "
    "2045. The disease is a leading cause of morbidity and mortality worldwide, contributing to "
    "complications including cardiovascular disease, chronic kidney disease, retinopathy, "
    "neuropathy, and lower limb amputations."
)
add_body(
    "Early identification of individuals at risk of developing T2DM is essential for implementing "
    "preventive measures such as lifestyle modifications, dietary interventions, and increased "
    "physical activity. Traditional risk assessment methods rely on clinical scoring systems such "
    "as the Finnish Diabetes Risk Score (FINDRISC) or the American Diabetes Association (ADA) risk "
    "test, which use a limited set of variables and fail to capture complex, non-linear "
    "interactions among risk factors."
)
add_body(
    "Recent advances in machine learning (ML) and artificial intelligence (AI) have demonstrated "
    "significant potential in improving the accuracy and scalability of disease risk prediction. "
    "ML models can analyze large volumes of clinical data, identify subtle patterns, and generate "
    "probabilistic risk estimates that surpass traditional statistical models. However, most "
    "existing ML-based diabetes prediction systems operate as monolithic, single-model pipelines "
    "that lack transparency, adaptability, and the ability to provide personalized, actionable "
    "clinical recommendations."
)
add_body(
    "The emergence of Large Language Models (LLMs) such as GPT-4, Google Gemini, and Claude has "
    "opened new possibilities for clinical decision support. LLMs can synthesize complex medical "
    "information, generate natural language explanations, and produce context-aware recommendations "
    "that are both clinically relevant and understandable to patients and healthcare providers. "
    "Furthermore, the paradigm of agentic AI, where multiple autonomous agents collaborate through "
    "shared state to solve complex tasks, represents a fundamental advancement over traditional "
    "pipeline architectures."
)

add_heading_styled("1.2 Problem Statement", 2)
add_body(
    "Despite the availability of machine learning models for diabetes risk prediction, several "
    "critical gaps remain in existing clinical decision-support systems:"
)
add_bullet("Lack of Transparency: Most ML models operate as black boxes, providing risk scores without explaining the underlying factors driving the prediction. Clinicians require interpretable explanations to trust and act upon AI-generated assessments.")
add_bullet("Absence of Personalization: Existing systems generate generic recommendations based on risk categories rather than tailoring advice to individual patient profiles, risk factors, and clinical context.")
add_bullet("Static Pipeline Architecture: Traditional systems process patient data through a fixed, linear pipeline without the ability to adapt, reason, or refine outputs based on changing patient conditions or longitudinal trends.")
add_bullet("No Longitudinal Monitoring: Most systems provide one-time risk assessments without tracking patient health metrics over time, detecting trends, or triggering alerts when conditions worsen.")
add_bullet("Limited Clinical Reasoning: Current systems lack the ability to perform autonomous reasoning over multi-dimensional patient data, synthesize outputs from multiple analytical components, and make context-aware decisions about care escalation.")
add_body(
    "There is a clear need for an intelligent, modular, and adaptive system that combines the "
    "predictive power of ML with the reasoning capabilities of LLMs within a multi-agent "
    "architecture that can provide transparent, personalized, and continuously updated clinical "
    "decision support for Type 2 Diabetes management."
)

add_heading_styled("1.3 Limitations of Existing Systems", 2)
add_body("A review of existing diabetes risk prediction systems reveals several limitations:")
add_bullet("Single-Model Approaches: Most systems rely on a single classifier (e.g., logistic regression or random forest) without comparing multiple models or leveraging ensemble methods for optimal performance.")
add_bullet("No Explainability Layer: Few systems integrate explainable AI techniques such as SHAP or LIME to provide feature-level explanations for individual predictions.")
add_bullet("Rule-Based Recommendations: Existing recommendation engines use static, rule-based templates that cannot adapt to individual patient contexts or evolving clinical guidelines.")
add_bullet("No Feedback Mechanism: There is no closed-loop system where monitoring results feed back into the recommendation engine to dynamically adjust advice based on patient progress.")
add_bullet("Monolithic Architecture: Traditional systems are tightly coupled, making it difficult to update, replace, or extend individual components without affecting the entire system.")

add_heading_styled("1.4 Motivation", 2)
add_body(
    "The motivation for this project stems from the convergence of several technological "
    "advancements and clinical needs. First, the increasing availability of structured health "
    "datasets such as the PIMA Indians Diabetes Dataset provides a foundation for training robust "
    "predictive models. Second, the maturation of explainable AI techniques, particularly SHAP, "
    "enables transparent and trustworthy model interpretations. Third, the rapid evolution of "
    "LLMs provides unprecedented capabilities for generating personalized, context-aware clinical "
    "recommendations in natural language. Finally, the emerging paradigm of agentic AI, where "
    "autonomous agents collaborate through shared state and feedback loops, offers a compelling "
    "framework for building modular, adaptive, and intelligent clinical decision-support systems."
)
add_body(
    "By combining these technologies within a unified multi-agent architecture, we aim to create "
    "a system that not only predicts diabetes risk with high accuracy but also explains its "
    "reasoning, generates personalized management plans, monitors patient progress over time, "
    "and autonomously adapts its recommendations based on evolving clinical context."
)

add_heading_styled("1.5 Objectives", 2)
add_body("The primary objectives of this project are:")
add_bullet("To design and implement a multi-agent AI system for Type 2 Diabetes risk stratification comprising five autonomous, collaborative agents.")
add_bullet("To train and evaluate multiple machine learning models (Logistic Regression, Random Forest, XGBoost) on the PIMA Indians Diabetes Dataset and select the best-performing model based on ROC-AUC.")
add_bullet("To integrate SHAP-based explainability to provide transparent, feature-level explanations for individual risk predictions.")
add_bullet("To leverage Google Gemini LLM via LangChain for generating personalized, clinically relevant lifestyle and dietary recommendations.")
add_bullet("To implement a stateful monitoring agent that tracks patient health metrics over time, detects trends, and generates clinical alerts.")
add_bullet("To build an orchestrator agent that uses LLM-based reasoning to autonomously evaluate system state and make decisions about care intensification or escalation.")
add_bullet("To develop an interactive Streamlit-based dashboard for real-time patient assessment and clinical decision support.")

add_heading_styled("1.6 Scope of the Project", 2)
add_body(
    "This project focuses on building a proof-of-concept agentic AI system for Type 2 Diabetes "
    "risk management. The scope includes: data ingestion and preprocessing from the PIMA dataset, "
    "ML-based risk prediction with multi-model comparison, SHAP-based explainability, LLM-powered "
    "recommendation generation, longitudinal monitoring with trend detection and alert systems, "
    "LLM-based orchestrator reasoning, and a web-based interactive dashboard. The system is "
    "designed as a decision-support tool and is explicitly not intended for medical diagnosis. "
    "The scope does not include integration with Electronic Health Record (EHR) systems, "
    "regulatory compliance (FDA/CE), or clinical validation through randomized controlled trials."
)

# ══════════════════════════════════════════════════════════════
# CHAPTER 2: LITERATURE REVIEW
# ══════════════════════════════════════════════════════════════
page_break()
add_heading_styled("Chapter 2: Literature Review", 1)

add_heading_styled("2.1 Machine Learning in Healthcare", 2)
add_body(
    "The application of machine learning in healthcare has grown significantly over the past "
    "decade, driven by the increasing availability of electronic health records, medical imaging "
    "data, and genomic information. ML algorithms have demonstrated superior performance in tasks "
    "such as disease diagnosis, prognosis, drug discovery, and treatment optimization compared to "
    "traditional statistical methods."
)
add_body(
    "Rajkomar et al. (2019) demonstrated that deep learning models could predict a range of "
    "clinical outcomes including in-hospital mortality, 30-day readmission, and length of stay "
    "using electronic health records from multiple hospitals. Esteva et al. (2019) provided a "
    "comprehensive review of deep learning applications in medicine, highlighting successes in "
    "dermatology, ophthalmology, and pathology. These studies established that ML could match or "
    "exceed specialist-level performance in specific clinical tasks."
)
add_body(
    "However, challenges remain in deploying ML models in clinical settings. Key concerns include "
    "model interpretability, data quality and bias, generalizability across populations, "
    "regulatory compliance, and the need for prospective clinical validation. The black-box "
    "nature of complex models such as deep neural networks and gradient boosting machines has "
    "been a significant barrier to clinical adoption."
)

add_heading_styled("2.2 Diabetes Prediction Systems", 2)
add_body(
    "Diabetes prediction using machine learning has been extensively studied. Kavakiotis et al. "
    "(2017) conducted a systematic review of ML applications in diabetes research, identifying "
    "studies using algorithms including support vector machines, random forests, naive Bayes, "
    "and neural networks. The PIMA Indians Diabetes Dataset, originally from the National "
    "Institute of Diabetes and Digestive and Kidney Diseases, has been one of the most widely "
    "used benchmarks in this domain."
)
add_body(
    "Sisodia and Sisodia (2018) compared naive Bayes, support vector machines, and decision "
    "trees on the PIMA dataset, achieving a best accuracy of 76.30% using naive Bayes. "
    "Zou et al. (2018) applied random forest and gradient boosting to diabetes prediction and "
    "reported improved performance with ensemble methods. More recently, studies have explored "
    "XGBoost, LightGBM, and deep learning architectures for diabetes risk prediction, consistently "
    "demonstrating that ensemble tree-based methods provide the best balance of accuracy and "
    "interpretability for tabular clinical data."
)
add_body(
    "Despite high predictive accuracy, most of these studies focus exclusively on classification "
    "performance and do not address the end-to-end clinical workflow including explainability, "
    "personalized recommendations, or longitudinal monitoring."
)

add_heading_styled("2.3 Explainable AI and SHAP", 2)
add_body(
    "Explainable AI (XAI) has become a critical requirement for deploying ML models in "
    "high-stakes domains such as healthcare. The European Union's General Data Protection "
    "Regulation (GDPR) has further emphasized the right to explanation for automated decisions "
    "affecting individuals."
)
add_body(
    "SHAP (SHapley Additive exPlanations), introduced by Lundberg and Lee (2017), provides a "
    "unified framework for interpreting model predictions based on Shapley values from cooperative "
    "game theory. SHAP assigns each feature an importance value (SHAP value) for a particular "
    "prediction, representing the feature's marginal contribution to the prediction outcome. "
    "SHAP offers several desirable properties including local accuracy, missingness, and "
    "consistency, making it theoretically grounded and practically useful."
)
add_body(
    "In diabetes prediction, SHAP has been used to identify key risk factors such as glucose "
    "levels, BMI, age, and family history. Studies by Lundberg et al. (2020) demonstrated that "
    "SHAP-based explanations improve clinician trust and understanding of ML predictions, leading "
    "to better clinical decision-making. The TreeExplainer variant provides exact, fast SHAP "
    "value computation for tree-based models such as Random Forest and XGBoost."
)

add_heading_styled("2.4 Large Language Models in Healthcare", 2)
add_body(
    "Large Language Models (LLMs) have emerged as powerful tools for healthcare applications. "
    "Models such as GPT-4, Google Gemini, Med-PaLM 2, and Claude have demonstrated strong "
    "performance on medical question answering, clinical reasoning, and patient communication "
    "tasks. Singhal et al. (2023) showed that Med-PaLM 2 achieved expert-level performance on "
    "the United States Medical Licensing Examination (USMLE) questions."
)
add_body(
    "In the context of clinical decision support, LLMs can be used to generate personalized "
    "health recommendations, summarize complex medical reports, and provide natural language "
    "explanations of analytical results. However, challenges include hallucination (generating "
    "plausible but incorrect information), the need for careful prompt engineering, and the "
    "importance of safety guardrails to prevent harmful medical advice."
)
add_body(
    "Frameworks such as LangChain enable structured interaction with LLMs through prompt "
    "templates, chains, and agents, facilitating the development of robust, production-ready "
    "LLM applications. Our system uses LangChain with Google Gemini to generate personalized "
    "recommendations and perform orchestrator-level clinical reasoning."
)

add_heading_styled("2.5 Multi-Agent Systems", 2)
add_body(
    "Multi-agent systems (MAS) consist of multiple autonomous agents that interact with each "
    "other and their environment to achieve individual or collective goals. In AI, the agentic "
    "paradigm has gained significant traction with the emergence of frameworks such as AutoGPT, "
    "CrewAI, and LangGraph, which enable LLM-powered agents to collaborate on complex tasks."
)
add_body(
    "The key advantages of multi-agent architectures over monolithic systems include: modularity "
    "(each agent handles a specific task), scalability (agents can be added or removed without "
    "affecting others), adaptability (agents can reason and adapt independently), and fault "
    "tolerance (failure of one agent does not necessarily crash the entire system). In healthcare, "
    "multi-agent systems have been explored for clinical workflow management, distributed "
    "decision-making, and collaborative diagnosis."
)
add_body(
    "Our system implements a five-agent architecture where each agent is an autonomous module "
    "with a specific responsibility. Agents communicate through a shared state dictionary, "
    "enabling both sequential processing and feedback loops. The Orchestrator Agent (Agent E) "
    "acts as a meta-agent that reasons over the outputs of all other agents to make autonomous "
    "decisions about care management."
)

add_heading_styled("2.6 Comparison with Existing Approaches", 2)
add_body("The following table compares our proposed system with existing approaches in literature:")
add_table(
    ["Feature", "Traditional ML", "ML + XAI", "Our Agentic System"],
    [
        ["Risk Prediction", "Yes", "Yes", "Yes (Multi-model)"],
        ["Explainability", "No", "Yes (SHAP/LIME)", "Yes (SHAP + NL)"],
        ["LLM Recommendations", "No", "No", "Yes (Gemini)"],
        ["Longitudinal Monitoring", "No", "No", "Yes (Stateful)"],
        ["Feedback Loop", "No", "No", "Yes (E to D)"],
        ["Autonomous Reasoning", "No", "No", "Yes (Orchestrator)"],
        ["Multi-Agent Architecture", "No", "No", "Yes (5 Agents)"],
        ["Interactive Dashboard", "Limited", "Limited", "Yes (Streamlit)"],
    ]
)

# ══════════════════════════════════════════════════════════════
# CHAPTER 3: REQUIREMENT ANALYSIS & SOLUTION APPROACH
# ══════════════════════════════════════════════════════════════
page_break()
add_heading_styled("Chapter 3: Requirement Analysis and Solution Approach", 1)

add_heading_styled("3.1 Functional Requirements", 2)
add_body("The system shall satisfy the following functional requirements:")
add_bullet("FR-1: The system shall accept patient health data including Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age as input.")
add_bullet("FR-2: The system shall validate and preprocess input data, handling missing values and deriving categorical features (BMI_Category, Glucose_Category).")
add_bullet("FR-3: The system shall predict diabetes risk probability and classify it into four risk levels: Low (0-25%), Moderate (25-50%), High (50-75%), and Very High (75-100%).")
add_bullet("FR-4: The system shall generate SHAP-based explanations identifying the top risk-increasing and risk-decreasing features for each prediction.")
add_bullet("FR-5: The system shall generate personalized dietary, exercise, and lifestyle recommendations using an LLM (Google Gemini).")
add_bullet("FR-6: The system shall track patient health metrics over multiple visits and detect improving, stable, or worsening trends.")
add_bullet("FR-7: The system shall generate clinical alerts when critical thresholds are crossed (e.g., Glucose > 180 mg/dL, BMI > 35).")
add_bullet("FR-8: The system shall perform autonomous orchestrator reasoning to evaluate whether recommendations should be intensified or care should be escalated.")
add_bullet("FR-9: The system shall provide a web-based dashboard for patient data entry, report viewing, and history tracking.")
add_bullet("FR-10: The system shall allow downloading assessment reports as PDF documents.")

add_heading_styled("3.2 Non-Functional Requirements", 2)
add_bullet("NFR-1: Performance: The ML prediction pipeline shall complete within 2 seconds for a single patient assessment.")
add_bullet("NFR-2: Scalability: The modular agent architecture shall allow adding new agents without modifying existing ones.")
add_bullet("NFR-3: Reliability: The system shall gracefully handle LLM API failures by falling back to template-based recommendations.")
add_bullet("NFR-4: Usability: The web interface shall use a modern glassmorphism design with clear visual hierarchy.")
add_bullet("NFR-5: Safety: All outputs shall include a medical disclaimer stating the system is for decision support only.")
add_bullet("NFR-6: Maintainability: Each agent shall be implemented as an independent Python class with clear interfaces.")

add_heading_styled("3.3 System Overview", 2)
add_body(
    "The proposed system follows a multi-agent architecture where five autonomous agents "
    "collaborate through a shared state dictionary. The pipeline processes patient data "
    "sequentially through ingestion, risk prediction, explainability, recommendation generation, "
    "and monitoring, with the Orchestrator Agent performing LLM-based meta-reasoning at the end."
)
add_body(
    "The system architecture follows this flow: Agent A (Data Ingestion) validates and preprocesses "
    "raw patient input. Agent B (Risk Stratification) uses a trained ML model to predict diabetes "
    "probability and risk level. Agent C (Explainability) computes SHAP values and generates "
    "natural language explanations. Agent D (Recommendation) uses Google Gemini to produce "
    "personalized clinical recommendations. Agent E (Monitoring and Orchestrator) tracks patient "
    "history, detects trends, generates alerts, and performs autonomous LLM-based reasoning "
    "over the full system state to decide on care intensification or escalation."
)
add_body(
    "All agents read from and write to a shared state dictionary, enabling information flow "
    "across the pipeline. The Orchestrator Agent can override or refine outputs from upstream "
    "agents, creating a closed-loop feedback mechanism that distinguishes this system from "
    "traditional linear pipelines."
)

add_heading_styled("3.4 Agent Descriptions", 2)

add_heading_styled("3.4.1 Agent A: Data Ingestion Agent", 3)
add_body(
    "The Data Ingestion Agent serves as the entry point of the agentic pipeline. It is "
    "responsible for loading raw patient data, performing data validation, handling missing "
    "values, and engineering derived features. The agent processes the PIMA Indians Diabetes "
    "Dataset, which contains 768 patient records with 8 clinical features and a binary outcome "
    "variable indicating diabetes diagnosis."
)
add_body(
    "Key operations performed by Agent A include: (1) replacing clinically invalid zero values "
    "in columns such as Glucose, BloodPressure, SkinThickness, Insulin, and BMI with NaN, "
    "(2) imputing missing values using median imputation (chosen for its robustness to outliers), "
    "(3) deriving two categorical features: BMI_Category (Normal, Overweight, Obese) based on "
    "WHO BMI classifications, and Glucose_Category (Normal, Prediabetic, Diabetic) based on "
    "American Diabetes Association thresholds, and (4) validating the processed dataset to ensure "
    "zero missing values, correct data types, and expected column structure."
)

add_heading_styled("3.4.2 Agent B: Risk Stratification Agent", 3)
add_body(
    "The Risk Stratification Agent is the core ML prediction engine of the system. It loads "
    "a pre-trained model from disk and uses it to predict diabetes risk probability for individual "
    "patients. The agent accepts patient data as a dictionary, pandas Series, or DataFrame, "
    "preprocesses it using the saved scaler and label encoders, and returns a probability score "
    "along with a categorical risk level."
)
add_body(
    "Risk levels are determined using the following thresholds: Low (0.00 - 0.25), Moderate "
    "(0.25 - 0.50), High (0.50 - 0.75), and Very High (0.75 - 1.00). The agent supports "
    "batch prediction for processing multiple patients and provides accessor methods for "
    "downstream agents to retrieve the model object, feature names, and risk threshold mappings."
)

add_heading_styled("3.4.3 Agent C: Explainability Agent", 3)
add_body(
    "The Explainability Agent generates transparent, clinician-friendly explanations for "
    "individual risk predictions using SHAP (SHapley Additive exPlanations). It initializes "
    "the appropriate SHAP explainer based on the model type: TreeExplainer for tree-based models "
    "(Random Forest, XGBoost), LinearExplainer for logistic regression, and KernelExplainer as "
    "a model-agnostic fallback."
)
add_body(
    "For each prediction, the agent computes per-feature SHAP values, identifies the top five "
    "risk-increasing (positive SHAP) and top five risk-decreasing (negative SHAP) features, "
    "and generates a structured natural language explanation. The explanation includes a risk "
    "assessment summary, key risk drivers with clinical context (e.g., 'elevated Glucose at "
    "180 mg/dL, in the prediabetic/diabetic range'), protective factors, and category-specific "
    "clinical guidance. The agent also provides visualization capabilities including SHAP "
    "summary plots and waterfall plots for individual predictions."
)

add_heading_styled("3.4.4 Agent D: Recommendation Agent", 3)
add_body(
    "The Recommendation Agent generates personalized health recommendations using Google Gemini "
    "LLM accessed through LangChain. The agent constructs a carefully engineered prompt that "
    "includes the patient's clinical data, predicted risk level, and SHAP-based explanation. "
    "The LLM then generates structured recommendations across four categories: Diet, Exercise, "
    "Lifestyle, and Warning."
)
add_body(
    "The prompt engineering includes strict safety rules that prevent the LLM from prescribing "
    "medications, acting as a medical diagnosis, or suggesting changes to existing medication "
    "regimens. In cases where the LLM API is unavailable (due to quota limits or network "
    "issues), the agent falls back to a template-based recommendation system that provides "
    "pre-defined advice based on the patient's risk category."
)

add_heading_styled("3.4.5 Agent E: Monitoring and Orchestrator Agent", 3)
add_body(
    "The Monitoring and Orchestrator Agent is the most complex and strategically important "
    "agent in the system. Unlike the other agents, which are stateless, Agent E maintains "
    "a per-patient history of observations across multiple visits, enabling longitudinal "
    "health monitoring."
)
add_body(
    "The monitoring component tracks clinical metrics (Glucose, BMI, BloodPressure, Insulin) "
    "over time and detects trends by comparing the last 2-3 observations. A metric is classified "
    "as worsening if it increases by more than 3%, improving if it decreases by more than 3%, "
    "or stable otherwise. The agent generates clinical alerts based on predefined rules: "
    "Very High risk triggers a critical alert, Glucose above 180 mg/dL triggers a high alert, "
    "risk escalation between visits triggers a warning, and a worsening trend triggers a "
    "monitoring alert."
)
add_body(
    "The orchestrator component uses Google Gemini LLM to perform autonomous clinical reasoning "
    "over the full system state, including patient data, risk prediction, SHAP explanation, "
    "initial recommendations from Agent D, trend analysis, and active alerts. The LLM evaluates "
    "whether current recommendations are sufficient and decides whether to maintain, intensify, "
    "or escalate the care plan. This meta-reasoning capability is what makes the system truly "
    "agentic rather than a simple sequential pipeline."
)

print("Part 2 complete: Chapters 1-3")
doc.save(OUTPUT_PATH)
print(f"Saved to {OUTPUT_PATH}")
