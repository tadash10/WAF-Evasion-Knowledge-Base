# get_evasion_technique.py
from app import db
from models import WafEvasionTechnique

def get_evasion_technique(technique_id):
    try:
        technique = WafEvasionTechnique.query.get(technique_id)
        if technique:
            return technique
        else:
            return None
    except Exception as e:
        return None
