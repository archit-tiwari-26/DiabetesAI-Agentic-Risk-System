import logging
import sys
from pprint import pprint

from src.main_pipeline import DiabetesAgentPipeline

# Configure logging to be less noisy for the test
logging.basicConfig(level=logging.WARNING)

def test_full_pipeline():
    print("=" * 60)
    print("🚀 INTEGRATION TEST: Full Multi-Agent Pipeline")
    print("=" * 60)
    
    # 1. Initialize Pipeline (loads all 5 agents)
    print("\n[Test] Initializing pipeline (loading models & agents)...")
    try:
        pipeline = DiabetesAgentPipeline()
        print("✅ Pipeline initialized successfully.")
    except Exception as e:
        print(f"❌ Failed to initialize pipeline: {e}")
        sys.exit(1)

    # 2. Define a mock patient input
    test_patient = {
        "Pregnancies": 2,
        "Glucose": 150.0,
        "BloodPressure": 85.0,
        "SkinThickness": 30.0,
        "Insulin": 120.0,
        "BMI": 29.5,
        "DiabetesPedigreeFunction": 0.65,
        "Age": 45
    }
    patient_id = "test_patient_999"

    print(f"\n[Test] Running pipeline for {patient_id}...")
    
    # 3. Process the patient through all agents
    try:
        final_state = pipeline.process_patient(test_patient, patient_id=patient_id)
        print("\n✅ Pipeline executed successfully.")
    except Exception as e:
        print(f"\n❌ Pipeline execution crashed: {e}")
        sys.exit(1)

    # 4. Verify agent interactions and state sharing
    print("\n" + "=" * 60)
    print("🧪 VERIFYING AGENT OUTPUTS & INTERACTIONS")
    print("=" * 60)

    success = True

    # Check Risk Agent (Agent B) output
    if "risk" in final_state and "probability" in final_state["risk"]:
        print(f"✅ Agent B (Risk): Generated probability {final_state['risk']['probability']:.4f} and level '{final_state['risk']['risk_level']}'")
    else:
        print("❌ Agent B (Risk) output missing from state!")
        success = False

    # Check Explainability Agent (Agent C) output
    if "explanation" in final_state and final_state["explanation"]:
        print(f"✅ Agent C (Explain): Generated SHAP explanation ({len(final_state['explanation'])} chars)")
    else:
        print("❌ Agent C (Explain) output missing from state!")
        success = False

    # Check Recommendation Agent (Agent D) output
    if "recommendation" in final_state and final_state["recommendation"]:
        print(f"✅ Agent D (Recommend): Generated base recommendation ({len(final_state['recommendation'])} chars)")
    else:
        print("❌ Agent D (Recommend) output missing from state!")
        success = False

    # Check Monitoring Agent (Agent E) updates & alerts
    if "trend" in final_state and "alerts" in final_state:
        print(f"✅ Agent E (Monitor/Alerts): Detected trend '{final_state['trend']}' and {len(final_state['alerts'])} alerts")
    else:
        print("❌ Agent E (Monitor/Alerts) output missing from state!")
        success = False

    # Check Orchestrator Reasoning (Agent E LLM)
    if "orchestrator_reasoning" in final_state and final_state["orchestrator_reasoning"]:
        print(f"✅ Agent E (Orchestrator): Reasoned over Agent D output and generated reasoning ({len(final_state['orchestrator_reasoning'])} chars)")
    else:
        print("❌ Agent E (Orchestrator) reasoning missing from state!")
        success = False

    if success:
        print("\n🎉 SUCCESS: All agents successfully interacted and populated the shared state!")
        print("\n--- Snippet of Final Shared State ---")
        # Print a clean snippet of the state dictionary
        summary_state = {
            "patient_id": final_state["patient_id"],
            "risk": final_state["risk"],
            "trend": final_state["trend"],
            "escalate": final_state["escalate"],
            "alerts_count": len(final_state["alerts"]),
            "explanation_snippet": final_state["explanation"].split('\n')[0] + "...",
            "recommendation_snippet": final_state["recommendation"][:50].replace('\n', ' ') + "...",
            "reasoning_snippet": final_state["orchestrator_reasoning"][:50].replace('\n', ' ') + "..."
        }
        pprint(summary_state)
    else:
        print("\n💥 FAILED: One or more agents failed to populate the shared state correctly.")
        sys.exit(1)

if __name__ == "__main__":
    test_full_pipeline()
