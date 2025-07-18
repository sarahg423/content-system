import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
COMPANY_PROFILE = {
    "name": os.getenv('COMPANY_NAME', 'Your Company'),
    "industry": os.getenv('COMPANY_INDUSTRY', 'SaaS Error Monitoring, Log Management, and Performance Monitoring'),
    "expertise": [
        "application performance monitoring and observability",
        "saas application scalability and extensibility", 
        "AI tools for managing SaaS applications",
        "Application Performance optimization",
        "Risk management for applications built using AI tools"
    ],
    "target_audience": os.getenv('TARGET_AUDIENCE', 'software engineers, small development teams, CTOs, high growth software startups')
}

AI_MONITORING_TOPICS = [
    "performance monitoring in an AI native fashion",
    "AI and log management best practices",
    "Finding issues in your codebase introduced by AI tools like Claude Code",
    "AI tools for stable and secure web applications",
    "Monolithic Architecture and AI best practices",
    "Production debugging techniques in an AI native software company",
    "Parts of your SDLC that can be automated or pushed to AI",
    "AI Prompts you should know to make your life as a software developer easier"
]

def validate_config():
    errors = []
    if not ANTHROPIC_API_KEY:
        errors.append("ANTHROPIC_API_KEY is required")
    return errors
