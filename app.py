from flask import Flask, flash, redirect, render_template, request, url_for
from flask import session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

from backend_files.python_files.classification import classify_text
from backend_files.python_files.summarization.summarization import generate_summary
from backend_files.python_files.summarization.highlight_entities import highlight_list_entities


app = Flask(__name__)

app.config['SECRET_KEY'] = 'cheie-secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)  
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#functie care verifica daca parola are cel putin 8 caractere, contine cel putin o cifra si cel putin un caracter special
def valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):  
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  
        return False
    return True

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    # Dacă utilizatorul este deja logat, îl redirecționăm direct
    if session.get('logged_in'):
        return redirect(url_for('text_page'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # Setăm sesiunea pentru utilizator
            session['logged_in'] = True
            session['username'] = username  # opțional, pentru afișare
            return redirect(url_for('text_page'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']  # corespunde cu numele din form
        
        has_error = False

        
        if not valid_password(password):
            flash("The password must be at least 8 characters long, contain at least one number, and one special character.","register")
            has_error = True

        if password != confirm_password:
            flash('Passwords do not match.', 'register')
            has_error = True

        if User.query.filter_by(username=username).first():
            flash('The username is already taken.', 'register')
            has_error = True

        if User.query.filter_by(email=email).first():
            flash('The email is already taken.', 'register')
            has_error = True

        if has_error:
            return render_template("register.html")

        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash(('Registration successful! Please log in.', 'success'),'register')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        input_text = request.form.get('text')
        task = request.form.get('task')
        highlight = request.form.get('highlight_entities')

        result = None
        if input_text:
            if task == 'classification':
                result = classify_text(input_text)
            elif task == 'summarization':
                result = generate_summary(input_text,20,100) 
                if highlight:
                    result = highlight_list_entities(result)


            session['result'] = result
        
        return redirect(url_for('process'))

    result = session.pop('result', None)
    return render_template('textPage.html', result=result)

# Ruta pentru pagina personalizata textPage.html
@app.route('/textpage')
def text_page():
    return render_template('textPage.html')

@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

if __name__ == '__main__':
    app.run(debug=True)
