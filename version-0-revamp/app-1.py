
from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from os import getenv, environ
from dotenv import load_dotenv
from datetime import timedelta, datetime
import re

# Load environment variables
load_dotenv()
app = Flask(__name__)

# Flask configurations
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = getenv('SECRET_KEY')

# Initialize database
db = SQLAlchemy(app)

# Password validation patterns
PASSWORD_PATTERNS = {
    'length': r'.{8,}',               # At least 8 characters
    'number': r'\d',                  # At least one digit
    'special': r'[!@#$%^&*(),.?":{}|<>]',  # At least one special character
    'case': r'(?=.*[a-z])(?=.*[A-Z])' # At least one uppercase and one lowercase letter
}

# Models
class Users(db.Model):
    """User model for the application."""
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        """Convert user object to dictionary for JSON responses."""
        return {
            'userId': self.userId,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# Utility functions
def validate_password(password):
    """Validate password against defined patterns."""
    validations = {
        'length': bool(re.search(PASSWORD_PATTERNS['length'], password)),
        'number': bool(re.search(PASSWORD_PATTERNS['number'], password)),
        'special': bool(re.search(PASSWORD_PATTERNS['special'], password)),
        'case': bool(re.search(PASSWORD_PATTERNS['case'], password))
    }
    return all(validations.values()), validations

def is_ajax_request():
    """Check if the request is AJAX."""
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def json_response(data, status=200):
    """Create a JSON response with the proper status."""
    response = jsonify(data)
    response.status_code = status
    return response

@app.before_request
def session_timeout_handler():
    """Handle session timeout."""
    if request.endpoint in ['static']:
        return

    now = datetime.utcnow()
    last_activity = session.get('last_activity')

    if last_activity:
        if isinstance(last_activity, str):
            last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")

        if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
            session.clear()
            flash('Your session has expired. Please log in again.', 'error')
            return redirect(url_for('logInExistingUser'))

    session['last_activity'] = now


# Routes
@app.route('/signup', methods=['GET', 'POST'])
def signUpNewUser():
    """Handle user registration."""
    if request.method == 'POST':
        data = request.form.to_dict()
        
        # Validate password
        is_valid_password, validations = validate_password(data.get('password', ''))
        if not is_valid_password:
            flash('Password does not meet requirements.', 'error')
            return redirect(url_for('signUpNewUser'))

        # Check if email already exists
        if Users.query.filter_by(email=data.get('email')).first():
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('signUpNewUser'))

        try:
            new_user = Users(
                firstname=data.get('firstname'),
                lastname=data.get('lastname'),
                email=data.get('email'),
                password=generate_password_hash(data.get('password'))
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('logInExistingUser'))
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error during signup: {e}")
            flash('An error occurred during registration. Please try again later.', 'error')
            return redirect(url_for('signUpNewUser'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def logInExistingUser():
    """Handle user login."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['userId'] = user.userId
            session['last_activity'] = datetime.utcnow()
            session.permanent = True
            flash('Logged in successfully!', 'success')
            return redirect(url_for('loggedInHomePage'))
        
        flash('Invalid email or password. Please try again.', 'error')
        return redirect(url_for('logInExistingUser'))

    return render_template('login.html')

@app.route('/')
def homePage():
    """Handle the home page."""
    if 'userId' in session:
        user = Users.query.get(session['userId'])
        return render_template('home.html', user=user)
    return render_template('index.html')

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('logInExistingUser'))

# Quiz routes (placeholders for now)
@app.route('/playquiz')
def quizPage():
    """Quiz selection page."""
    return render_template('choosequiz.html')

@app.route('/random-quiz')
def randomQuiz():
    """Random quiz page."""
    return render_template('singlequiz.html')

@app.route('/profile')
def userProfile():
    """User profile page."""
    return render_template('comingsoon.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
