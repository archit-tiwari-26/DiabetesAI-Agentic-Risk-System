"""Test Agent D: Recommendation Agent with Google Gemini LLM."""
import logging, sys
logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(name)s  %(levelname)s  %(message)s", stream=sys.stdout)

from src.agents.recommendation_agent import RecommendationAgent

print("\n" + "=" * 65)
print("  🤖 AGENT D — Recommendation Agent Test (Gemini LLM)")
print("=" * 65)

agent = RecommendationAgent()
print(f"\nLLM available: {agent.llm_available}")
print(f"Chain built:   {agent.chain is not None}")

if not agent.llm_available:
    print("❌ LLM not available — check .env")
    sys.exit(1)

# ── Test 1: High-risk patient ────────────────────────────────────
patient = {
    "Glucose": 180, "BMI": 32, "Age": 50,
    "BloodPressure": 85, "Insulin": 200,
    "DiabetesPedigreeFunction": 0.6, "Pregnancies": 3,
}

print("\n" + "-" * 65)
print("TEST 1: High-Risk Patient")
print("-" * 65)

output = agent.generate(
    patient_data=patient,
    risk_level="High",
    explanation="High glucose (180 mg/dL) and elevated BMI (32) are the "
                "major contributing factors. Family history score is also elevated.",
)
print(output)

# ── Test 2: Low-risk patient ─────────────────────────────────────
patient_low = {
    "Glucose": 85, "BMI": 22, "Age": 25,
    "BloodPressure": 66, "Insulin": 80,
    "DiabetesPedigreeFunction": 0.15, "Pregnancies": 1,
}

print("\n" + "-" * 65)
print("TEST 2: Low-Risk Patient")
print("-" * 65)

output2 = agent.generate(
    patient_data=patient_low,
    risk_level="Low",
    explanation="All metrics are within normal range. Low family history score.",
)
print(output2)

print("\n" + "=" * 65)
print("  ✅ AGENT D TESTS COMPLETE")
print("=" * 65)
