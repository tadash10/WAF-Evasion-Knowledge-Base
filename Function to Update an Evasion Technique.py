# update_evasion_technique.py
from app import db
from models import WafEvasionTechnique

def update_evasion_technique(technique_id, name, description, example):
    try:
        technique = WafEvasionTechnique.query.get(technique_id)
        if technique:
            technique.name = name
            technique.description = description
            technique.example = example
            db.session.commit()
            return True, "Technique updated successfully"
        else:
            return False, "Technique not found"
    except Exception as e:
        return False, f"An error occurred: {str(e)}"
