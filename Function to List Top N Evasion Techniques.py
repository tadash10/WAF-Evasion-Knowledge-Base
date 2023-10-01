# list_top_evasion_techniques.py
from app import db
from models import WafEvasionTechnique

def list_top_evasion_techniques(top_n=10):
    try:
        techniques = WafEvasionTechnique.query.limit(top_n).all()
        return techniques
    except Exception as e:
        return [], f"An error occurred: {str(e)}"
