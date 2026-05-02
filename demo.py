"""
Simple demonstration script for the Diabetes AI Agent System.

This script showcases the complete agentic pipeline in action.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.main_pipeline import DiabetesAIAgentsPipeline


def main():
    """Run the complete demonstration."""
    
    print("\n" + "=" * 80)
    print(" " * 15 + "🏥 DIABETES AI AGENT SYSTEM - DEMONSTRATION")
    print("=" * 80)
    
    print("""
    This demonstration showcases a multi-agent agentic AI system with 5 agents:
    
    1. 📥 Ingestion Agent     - Data loading and preprocessing
    2. 🎯 Risk Agent          - Risk prediction using ML models
    3. 🔍 Explainability Agent - SHAP-based model interpretability
    4. 💡 Recommendation Agent - Personalized care recommendations
    5. 📈 Monitoring Agent     - Longitudinal patient tracking
    
    The agents collaborate to provide comprehensive diabetes risk assessment
    and personalized management recommendations.
    """)
    
    print("=" * 80)
    print("STARTING PIPELINE...")
    print("=" * 80 + "\n")
    
    # Create and run pipeline
    pipeline = DiabetesAIAgentsPipeline()
    
    # Run complete pipeline with model training
    results = pipeline.run_complete_pipeline(train_model=True)
    
    # Print summary
    if results["status"] == "success":
        print("\n" + "=" * 80)
        print("✅ DEMONSTRATION COMPLETED SUCCESSFULLY")
        print("=" * 80)
        
        print("""
        Pipeline executed all 5 agents successfully:
        ✓ Ingestion Agent     - Data prepared and validated
        ✓ Risk Agent          - Predictions generated
        ✓ Explainability Agent - SHAP explanations created
        ✓ Recommendation Agent - Personalized plans generated
        ✓ Monitoring Agent     - Patient tracking activated
        
        Next Steps:
        1. Check logs/diabetes_ai_system.log for detailed logs
        2. Run Jupyter notebooks for EDA and model training
        3. Launch Streamlit app: streamlit run app/streamlit_app.py
        4. Explore the src/agents/ modules for implementation details
        """)
    else:
        print(f"\n❌ Pipeline failed: {results.get('error', 'Unknown error')}")
    
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
