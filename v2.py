from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///waf_evasion.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for session security
db = SQLAlchemy(app)

class WafEvasionTechnique(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    example = db.Column(db.Text, nullable=True)

@app.route('/')
def list_evasion_techniques():
    try:
        evasion_techniques = WafEvasionTechnique.query.all()
        return render_template('list_evasion_techniques.html', techniques=evasion_techniques)
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'danger')
        return redirect(url_for('list_evasion_techniques'))

@app.route('/add', methods=['GET', 'POST'])
def add_evasion_technique():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            example = request.form['example']

            technique = WafEvasionTechnique(name=name, description=description, example=example)
            db.session.add(technique)
            db.session.commit()
            flash('Technique added successfully', 'success')
            return redirect(url_for('list_evasion_techniques'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')
            return redirect(url_for('add_evasion_technique'))
    return render_template('add_evasion_technique.html')

@app.route('/technique/<int:id>')
def view_evasion_technique(id):
    try:
        technique = WafEvasionTechnique.query.get(id)
        return render_template('view_evasion_technique.html', technique=technique)
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'danger')
        return redirect(url_for('list_evasion_techniques'))

if __name__ == '__main__':
    try:
        db.create_all()
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
