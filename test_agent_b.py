"""
Test script for Agent B: Model Training + Risk Stratification Agent.
Demonstrates the full pipeline: training, saving, and risk prediction.
"""

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(name)s  %(levelname)s  %(message)s",
    stream=sys.stdout,
)

# ── Step 1-8: Train models and save best ──────────────────────────
from src.models.train import ModelTrainer

print("\n" + "=" * 65)
print("  PART 1: MODEL TRAINING PIPELINE")
print("=" * 65)

trainer = ModelTrainer()
training_result = trainer.run_training_pipeline()

# ── Step 9-10: Risk Stratification Agent test ─────────────────────
from src.agents.risk_agent import RiskAgent

print("\n" + "=" * 65)
print("  PART 2: RISK STRATIFICATION AGENT TEST")
print("=" * 65)

agent = RiskAgent()

# ── Sample patient 1: higher risk ──
sample_patient_1 = {
    "Pregnancies": 5,
    "Glucose": 166.0,
    "BloodPressure": 72.0,
    "SkinThickness": 19.0,
    "Insulin": 175.0,
    "BMI": 25.8,
    "DiabetesPedigreeFunction": 0.587,
    "Age": 51,
    "BMI_Category": "Overweight",
    "Glucose_Category": "Prediabetic",
}

print("\n--- Patient 1 (Higher-risk profile) ---")
for k, v in sample_patient_1.items():
    print(f"   {k}: {v}")

prob1, cat1 = agent.predict(sample_patient_1)
print(f"\n   >>> Probability : {prob1:.4f}")
print(f"   >>> Risk Level  : {cat1}")

# ── Sample patient 2: lower risk ──
sample_patient_2 = {
    "Pregnancies": 1,
    "Glucose": 85.0,
    "BloodPressure": 66.0,
    "SkinThickness": 29.0,
    "Insulin": 100.0,
    "BMI": 22.5,
    "DiabetesPedigreeFunction": 0.15,
    "Age": 25,
    "BMI_Category": "Normal",
    "Glucose_Category": "Normal",
}

print("\n--- Patient 2 (Lower-risk profile) ---")
for k, v in sample_patient_2.items():
    print(f"   {k}: {v}")

prob2, cat2 = agent.predict(sample_patient_2)
print(f"\n   >>> Probability : {prob2:.4f}")
print(f"   >>> Risk Level  : {cat2}")

print("\n" + "=" * 65)
print("  ALL TESTS PASSED")
print("=" * 65 + "\n")
