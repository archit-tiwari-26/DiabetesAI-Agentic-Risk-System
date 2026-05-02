"""Test script for Agent C: Explainability & Clinical Transparency Agent."""
import logging, sys
logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(name)s  %(levelname)s  %(message)s", stream=sys.stdout)

from src.agents.explainability_agent import ExplainabilityAgent

agent = ExplainabilityAgent()

# ── Test 1: High-risk patient ───────────────────────────────────────
sample_high = {
    "Pregnancies": 5, "Glucose": 166.0, "BloodPressure": 72.0,
    "SkinThickness": 19.0, "Insulin": 175.0, "BMI": 25.8,
    "DiabetesPedigreeFunction": 0.587, "Age": 51,
    "BMI_Category": "Overweight", "Glucose_Category": "Prediabetic",
}

print("\n" + "=" * 65)
print("  TEST 1: High-Risk Patient Explanation")
print("=" * 65)
r1 = agent.explain(sample_high)
print(f"\nProbability: {r1['probability']:.4f}  |  Risk: {r1['risk_category']}")
print("\nTop Risk-Increasing Features:")
for f, v in r1["top_positive_features"]:
    print(f"   {f:30s}  SHAP={v:+.4f}")
print(f"\n{r1['explanation_text']}")

# ── Test 2: Low-risk patient ────────────────────────────────────────
sample_low = {
    "Pregnancies": 1, "Glucose": 85.0, "BloodPressure": 66.0,
    "SkinThickness": 29.0, "Insulin": 100.0, "BMI": 22.5,
    "DiabetesPedigreeFunction": 0.15, "Age": 25,
    "BMI_Category": "Normal", "Glucose_Category": "Normal",
}

print("\n" + "=" * 65)
print("  TEST 2: Low-Risk Patient Explanation")
print("=" * 65)
r2 = agent.explain(sample_low)
print(f"\nProbability: {r2['probability']:.4f}  |  Risk: {r2['risk_category']}")
print(f"\n{r2['explanation_text']}")

# ── Test 3: Generate plots ──────────────────────────────────────────
print("\n" + "=" * 65)
print("  TEST 3: SHAP Visualisations")
print("=" * 65)
s = agent.generate_summary_plot()
w = agent.generate_waterfall_plot(sample_high)
print(f"Summary plot:   {'✅ ' + s if s else '❌ failed'}")
print(f"Waterfall plot: {'✅ ' + w if w else '❌ failed'}")

print("\n" + "=" * 65)
print("  ✅ ALL AGENT C TESTS COMPLETE")
print("=" * 65)
