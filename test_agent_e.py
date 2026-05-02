"""
Test Agent E: Monitoring & Follow-up Orchestrator.

Simulates 3 patient visits with worsening metrics, then demonstrates:
  1. Trend detection
  2. Alert generation
  3. Recommendation adjustment
  4. Feedback loop (calls back into Agent D / Gemini LLM)
"""
import logging, sys
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s  %(name)s  %(levelname)s  %(message)s",
                    stream=sys.stdout)

from src.agents.monitoring_agent import MonitoringAgent
from src.agents.recommendation_agent import RecommendationAgent

# ── Initialize agents ────────────────────────────────────────────────
monitor = MonitoringAgent()
rec_agent = RecommendationAgent()

print("\n" + "=" * 65)
print("  🔁 AGENT E — Full Monitoring & Feedback Loop Test")
print("=" * 65)

# ── Simulate 3 visits: progressively worsening ──────────────────────
visits = [
    ({"Glucose": 130, "BMI": 28, "BloodPressure": 78, "Insulin": 120,
      "Age": 50, "Pregnancies": 3, "DiabetesPedigreeFunction": 0.4},
     "Moderate"),
    ({"Glucose": 160, "BMI": 30, "BloodPressure": 85, "Insulin": 150,
      "Age": 50, "Pregnancies": 3, "DiabetesPedigreeFunction": 0.4},
     "High"),
    ({"Glucose": 195, "BMI": 33, "BloodPressure": 92, "Insulin": 210,
      "Age": 50, "Pregnancies": 3, "DiabetesPedigreeFunction": 0.4},
     "Very High"),
]

for i, (data, risk) in enumerate(visits, 1):
    monitor.update(data, risk)
    print(f"\n📋 Visit {i}: risk={risk}, Glucose={data['Glucose']}, BMI={data['BMI']}")

# ── Test 1: Trend Analysis ──────────────────────────────────────────
print("\n" + "-" * 65)
print("TEST 1: Trend Analysis")
print("-" * 65)

trend = monitor.analyze_trend()
print(f"Overall trend: {trend['overall']}")
for m, info in trend.get("metric_trends", {}).items():
    print(f"  {m:16s} {info['direction']:10s} ({info['pct_change']:+.1f}%) "
          f"[{info['first']} → {info['last']}]")
print(f"  Risk trend:      {trend['risk_trend']}")

# ── Test 2: Alerts ──────────────────────────────────────────────────
print("\n" + "-" * 65)
print("TEST 2: Alert Generation")
print("-" * 65)

alerts = monitor.generate_alerts()
print(f"Alerts generated: {len(alerts)}")
for a in alerts:
    print(f"  [{a['severity'].upper():8s}] {a['message']}")
    print(f"             → {a['action']}")

# ── Test 3: Recommendation Adjustment ───────────────────────────────
print("\n" + "-" * 65)
print("TEST 3: Recommendation Adjustment (without LLM)")
print("-" * 65)

base_rec = ("Diet: Eat more vegetables and whole grains.\n"
            "Exercise: Walk 30 minutes daily.\n"
            "Lifestyle: Sleep 7-8 hours.")
adjusted = monitor.adjust_recommendation(base_rec)
print(adjusted)

# ── Test 4: Full Feedback Loop (with LLM) ───────────────────────────
print("\n" + "-" * 65)
print("TEST 4: Feedback Loop → Agent D (Gemini LLM)")
print("-" * 65)

if rec_agent.llm_available:
    latest_data = visits[-1][0]
    latest_risk = visits[-1][1]
    explanation = ("Patient shows Very High risk driven by critically elevated "
                   "Glucose (195 mg/dL), elevated BMI (33), and rising Insulin.")

    final_rec = monitor.feedback_loop(
        recommendation_agent=rec_agent,
        patient_data=latest_data,
        risk_level=latest_risk,
        explanation=explanation,
    )
    print(final_rec)
else:
    print("⚠️ LLM not available — skipping feedback loop test.")
    print("   (Set GOOGLE_API_KEY in .env to enable)")

# ── Test 5: run_pipeline (backward compat) ───────────────────────────
print("\n" + "-" * 65)
print("TEST 5: run_pipeline() (main_pipeline compatibility)")
print("-" * 65)

report = monitor.run_pipeline(
    patient_id="PATIENT_TEST",
    current_risk_score=0.82,
    current_metrics=visits[-1][0],
    previous_risk_score=0.55,
)
print(f"Status: {report['status']}")
print(f"Alerts: {report['num_alerts']}")
print(f"Trend:  {report['trend_analysis'].get('overall', 'n/a')}")
print(f"Action: {report['recommendation']}")

print("\n" + "=" * 65)
print("  ✅ ALL AGENT E TESTS COMPLETE")
print("=" * 65)
