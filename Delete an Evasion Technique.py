# delete_evasion_technique.py
from app import db
from models import WafEvasionTechnique

def delete_evasion_technique(technique_id):
    try:
        technique = WafEvasionTechnique.query.get(technique_id)
        if technique:
            db.session.delete(technique)
            db.session.commit()
            return True, "Technique deleted successfully"
        else:
            return False, "Technique not found"
    except Exception as e:
        return False, f"An error occurred: {str(e)}"
