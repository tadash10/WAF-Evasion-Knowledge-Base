# search_evasion_techniques.py
from app import db
from models import WafEvasionTechnique

def search_evasion_techniques(keyword):
    try:
        techniques = WafEvasionTechnique.query.filter(
            WafEvasionTechnique.name.ilike(f"%{keyword}%") |
            WafEvasionTechnique.description.ilike(f"%{keyword}%") |
            WafEvasionTechnique.example.ilike(f"%{keyword}%")
        ).all()
        return techniques
    except Exception as e:
        return [], f"An error occurred: {str(e)}"
