import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
COMPANY_PROFILE = {
    "name": os.getenv('COMPANY_NAME', 'Your AI Monitoring Company'),
    "industry": os.getenv('COMPANY_INDUSTRY', 'AI SaaS Monitoring'),
    "expertise": [
        "AI model monitoring and observability",
        "ML pipeline reliability", 
        "AI governance and compliance",
        "Performance optimization",
        "Risk management for AI systems"
    ],
    "target_audience": os.getenv('TARGET_AUDIENCE', 'AI engineers, ML teams, CTOs')
}

AI_MONITORING_TOPICS = [
    "AI model drift detection and prevention",
    "Real-time ML pipeline monitoring",
    "Model performance optimization strategies",
    "AI governance frameworks for enterprise",
    "ML observability best practices",
    "Production AI debugging techniques",
    "Automated model retraining workflows",
    "AI system reliability engineering"
]

def validate_config():
    errors = []
    if not ANTHROPIC_API_KEY:
        errors.append("ANTHROPIC_API_KEY is required")
    return errors
