"""Test Agent A: Data Ingestion & Preprocessing Agent."""
import logging, sys
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s  %(name)s  %(levelname)s  %(message)s",
                    stream=sys.stdout)

from src.agents.ingestion_agent import IngestionAgent

print("\n" + "=" * 65)
print("  📥 AGENT A — Data Ingestion & Preprocessing Test")
print("=" * 65)

agent = IngestionAgent(
    input_path="data/raw/diabetes.csv",
    output_path="data/processed/cleaned_diabetes.csv",
)

df = agent.run()

# ── Verification checks ─────────────────────────────────────────────
print("\n" + "-" * 65)
print("VERIFICATION")
print("-" * 65)

# 1. No missing values
missing = df.isnull().sum().sum()
print(f"1. Missing values: {missing} {'✅' if missing == 0 else '❌'}")

# 2. New features present
has_bmi_cat = "BMI_Category" in df.columns
has_gluc_cat = "Glucose_Category" in df.columns
print(f"2. BMI_Category present: {'✅' if has_bmi_cat else '❌'}")
print(f"3. Glucose_Category present: {'✅' if has_gluc_cat else '❌'}")

# 3. No invalid zeros in clinical columns
for col in ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]:
    zeros = (df[col] == 0).sum()
    print(f"4. {col} zeros remaining: {zeros} {'✅' if zeros == 0 else '❌'}")

# 4. Shape
print(f"5. Shape: {df.shape}")

# 5. Data types
print(f"6. Target (Outcome) present: {'✅' if 'Outcome' in df.columns else '❌'}")

# 6. Saved file
import os
saved = os.path.exists("data/processed/cleaned_diabetes.csv")
print(f"7. File saved: {'✅' if saved else '❌'}")

# 7. Head
print(f"\nHead:\n{df.head(3).to_string()}")

print("\n" + "=" * 65)
print("  ✅ AGENT A TEST COMPLETE")
print("=" * 65)
