# # from flask import Flask, render_template, request, flash, redirect, session, url_for
# # from flask_sqlalchemy import SQLAlchemy
# # from werkzeug.security import generate_password_hash, check_password_hash
# # from os import getenv, environ
# # from dotenv import load_dotenv
# # from datetime import timedelta, datetime, timezone

# # # Load the environment variables
# # load_dotenv()
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
# # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Set session timeout to 30 minute
# # app.secret_key = getenv('SECRET_KEY')
# # db = SQLAlchemy(app)


# # # User model
# # class Users(db.Model):
# #     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     firstname = db.Column(db.String(50), nullable=False)
# #     lastname = db.Column(db.String(50), nullable=False)
# #     email = db.Column(db.String(100), nullable=False, unique=True)
# #     password = db.Column(db.String(100), nullable=False)


# # @app.before_request
# # def session_timeout_handler():
# #     now = datetime.utcnow()  # Naive datetime (UTC)
# #     last_activity = session.get('last_activity')

# #     if last_activity:
# #         if isinstance(last_activity, str):
# #             # Parse last_activity if it's stored as a string
# #             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
# #         # Ensure both datetime objects are naive
# #         last_activity = last_activity.replace(tzinfo=None)

# #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# #             session.pop('userId', None)
# #             session.pop('last_activity', None)
# #             flash('Your session has expired. Please log in again.', 'error')
# #             return redirect('/login')

# #     # Update last_activity to the current time (store naive UTC datetime)
# #     session['last_activity'] = now


# # @app.route('/')
# # def homePage():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         return render_template('home.html', user=user)
# #     return render_template('index.html')


# # # Handling error pages or wrong redirections
# # @app.errorhandler(404)
# # def page_not_found(e):
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         # return render_template('comingsoon.html', user=user)
# #         return render_template('404.html', user=user), 404
# #     return redirect('/login')


# # @app.route('/signup', methods=['GET', 'POST'])
# # def signUpNewUser():
# #     if request.method == 'POST':
# #         UserFirstName = request.form['firstname']
# #         UserLastName = request.form['lastname']
# #         UserEmail = request.form['email']
# #         UserPassword = request.form['password']
# #         hashed_password = generate_password_hash(UserPassword)
# #         new_user = Users(firstname=UserFirstName, lastname=UserLastName, email=UserEmail, password=hashed_password)
# #         try:
# #             db.session.add(new_user)
# #             db.session.commit()
# #             flash('Registration successful! Please log in.', 'success')
# #             return redirect('/login')
# #         except:
# #             flash('Email already registered. Please log in.', 'error')
# #             return redirect('/signup')
# #     return render_template('signup.html')


# # @app.route('/login', methods=['GET', 'POST'])
# # def logInExistingUser():
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         password = request.form['password']
# #         user = Users.query.filter_by(email=email).first()
# #         if user and check_password_hash(user.password, password):
# #             session['userId'] = user.userId
# #             session['last_activity'] = datetime.utcnow()  # Initialize last activity timestamp
# #             session.permanent = True  # Mark session as permanent
# #             flash('Logged in successfully!', 'success')
# #             return redirect('/home')
# #         flash('Invalid email or password. Please try again.', 'error')
# #         return redirect('/login')
# #     return render_template('login.html')


# # @app.route('/home')
# # def loggedInHomePage():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         return render_template('home.html', user=user)
# #     flash('You must be logged in to access the home page.', 'error')
# #     return redirect('/login')


# # @app.route('/playquiz')
# # def quizPage():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         return render_template('choosequiz.html', user=user)
# #     return redirect('/login')


# # @app.route('/multiquiz')
# # def multiquiz():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         return render_template('multiquiz.html', user=user)
# #     return redirect('/login')


# # @app.route('/random-quiz')
# # def singlequizquiz():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         return render_template('singlequiz.html', user=user)
# #     return redirect('/login')


# # # Implement this route to handle the quiz submission
# # @app.route('/my-quizzes')
# # def myQuizzes():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         return render_template('comingsoon.html', user=user)
# #     return redirect('/login')


# # @app.route('/profile')
# # def userProfile():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         return render_template('comingsoon.html', user=user)
# #     return redirect('/login')

# # @app.route('/leaderboard')
# # def leaderboard():
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         flash('Login successful! Welcome to your home!', 'success')
# #         return render_template('comingsoon.html', user=user)
# #     return redirect('/login')


# # @app.route('/logout')
# # def logout():
# #     session.pop('userId', None)
# #     session.pop('last_activity', None)  # Clear last activity timestamp
# #     flash('You have been logged out.', 'info')
# #     return redirect('/login')


# # if __name__ == '__main__':
# #     port = int(environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
# #     app.run(host="0.0.0.0", port=port)
# #     # app.run(debug=True, port=5000)


# # from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
# # from flask_sqlalchemy import SQLAlchemy
# # from werkzeug.security import generate_password_hash, check_password_hash
# # from os import getenv, environ
# # from dotenv import load_dotenv
# # from datetime import timedelta, datetime, timezone
# # import re

# # # Load the environment variables
# # load_dotenv()
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
# # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# # app.secret_key = getenv('SECRET_KEY')
# # db = SQLAlchemy(app)


# # # Password validation regex patterns
# # PASSWORD_PATTERNS = {
# #     'length': r'.{8,}',
# #     'number': r'\d',
# #     'special': r'[!@#$%^&*(),.?":{}|<>]',
# #     'case': r'(?=.*[a-z])(?=.*[A-Z])'
# # }


# # class Users(db.Model):
# #     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     firstname = db.Column(db.String(50), nullable=False)
# #     lastname = db.Column(db.String(50), nullable=False)
# #     email = db.Column(db.String(100), nullable=False, unique=True)
# #     password = db.Column(db.String(100), nullable=False)


# # def validate_password(password):
# #     """Validate password against defined patterns"""
# #     return all(
# #         bool(re.search(pattern, password))
# #         for pattern in PASSWORD_PATTERNS.values()
# #     )


# # def is_ajax_request():
# #     """Check if the request is an AJAX request"""
# #     return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


# # @app.before_request
# # def session_timeout_handler():
# #     if request.endpoint in ['static']:
# #         return

# #     now = datetime.utcnow()
# #     last_activity = session.get('last_activity')

# #     if last_activity:
# #         if isinstance(last_activity, str):
# #             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
# #         last_activity = last_activity.replace(tzinfo=None)

# #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# #             session.pop('userId', None)
# #             session.pop('last_activity', None)
# #             if is_ajax_request():
# #                 return jsonify({'error': 'session_expired', 'message': 'Your session has expired. Please log in again.'}), 401
# #             flash('Your session has expired. Please log in again.', 'error')
# #             return redirect('/login')

# #     session['last_activity'] = now


# # @app.route('/signup', methods=['GET', 'POST'])
# # def signUpNewUser():
# #     if request.method == 'POST':
# #         UserFirstName = request.form['firstname']
# #         UserLastName = request.form['lastname']
# #         UserEmail = request.form['email']
# #         UserPassword = request.form['password']

# #         # Validate password
# #         if not validate_password(UserPassword):
# #             if is_ajax_request():
# #                 return jsonify({
# #                     'error': 'invalid_password',
# #                     'message': 'Password does not meet requirements'
# #                 }), 400
# #             flash('Password does not meet requirements', 'error')
# #             return redirect('/signup')

# #         # Check if email exists
# #         if Users.query.filter_by(email=UserEmail).first():
# #             if is_ajax_request():
# #                 return jsonify({
# #                     'error': 'email_exists',
# #                     'message': 'Email already exists in our records'
# #                 }), 400
# #             flash('Email already registered. Please log in.', 'error')
# #             return redirect('/signup')

# #         try:
# #             hashed_password = generate_password_hash(UserPassword)
# #             new_user = Users(
# #                 firstname=UserFirstName,
# #                 lastname=UserLastName,
# #                 email=UserEmail,
# #                 password=hashed_password
# #             )
# #             db.session.add(new_user)
# #             db.session.commit()

# #             if is_ajax_request():
# #                 return jsonify({
# #                     'message': 'Registration successful! Please log in.',
# #                     'redirect': '/login'
# #                 }), 200
# #             flash('Registration successful! Please log in.', 'success')
# #             return redirect('/login')
# #         except Exception as e:
# #             db.session.rollback()
# #             if is_ajax_request():
# #                 return jsonify({
# #                     'error': 'server_error',
# #                     'message': 'An error occurred during registration'
# #                 }), 500
# #             flash('An error occurred during registration', 'error')
# #             return redirect('/signup')

# #     return render_template('signup.html')


# # @app.route('/login', methods=['GET', 'POST'])
# # def logInExistingUser():
# #     if request.method == 'POST':
# #         email = request.form['email']
# #         password = request.form['password']
# #         user = Users.query.filter_by(email=email).first()

# #         if user and check_password_hash(user.password, password):
# #             session['userId'] = user.userId
# #             session['last_activity'] = datetime.utcnow()
# #             session.permanent = True

# #             if is_ajax_request():
# #                 return jsonify({
# #                     'message': 'Logged in successfully!',
# #                     'redirect': '/home'
# #                 }), 200
# #             flash('Logged in successfully!', 'success')
# #             return redirect('/home')

# #         if is_ajax_request():
# #             return jsonify({
# #                 'error': 'invalid_credentials',
# #                 'message': 'Incorrect email or password'
# #             }), 401
# #         flash('Invalid email or password. Please try again.', 'error')
# #         return redirect('/login')


# #     return render_template('login.html')

# # # The rest of your routes remain the same, but you might want to add AJAX handling
# # # to them as well if needed


# # @app.errorhandler(404)
# # def page_not_found(e):
# #     if is_ajax_request():
# #         return jsonify({'error': 'not_found', 'message': 'Page not found'}), 404
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         return render_template('404.html', user=user), 404
# #     return redirect('/login')


# # @app.errorhandler(500)
# # def internal_error(e):
# #     if is_ajax_request():
# #         return jsonify({'error': 'server_error', 'message': 'An internal error occurred'}), 500
# #     flash('An internal error occurred', 'error')
# #     return redirect('/login')


# # if __name__ == '__main__':
# #     port = int(environ.get("PORT", 5000))
# #     app.run(host="0.0.0.0", port=port)


# from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from os import getenv, environ
# from dotenv import load_dotenv
# from datetime import timedelta, datetime, timezone
# import re
# import json

# # Load environment variables
# load_dotenv()
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = getenv('SECRET_KEY')
# db = SQLAlchemy(app)

# # Password validation patterns
# PASSWORD_PATTERNS = {
#     'length': r'.{8,}',
#     'number': r'\d',
#     'special': r'[!@#$%^&*(),.?":{}|<>]',
#     'case': r'(?=.*[a-z])(?=.*[A-Z])'
# }

# class Users(db.Model):
#     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     firstname = db.Column(db.String(50), nullable=False)
#     lastname = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(100), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
#     def to_dict(self):
#         return {
#             'userId': self.userId,
#             'firstname': self.firstname,
#             'lastname': self.lastname,
#             'email': self.email,
#             'created_at': self.created_at.isoformat()
#         }

# def validate_password(password):
#     """Validate password against defined patterns"""
#     validations = {
#         'length': bool(re.search(PASSWORD_PATTERNS['length'], password)),
#         'number': bool(re.search(PASSWORD_PATTERNS['number'], password)),
#         'special': bool(re.search(PASSWORD_PATTERNS['special'], password)),
#         'case': bool(re.search(PASSWORD_PATTERNS['case'], password))
#     }
#     return all(validations.values()), validations

# def is_ajax_request():
#     """Check if request is AJAX"""
#     return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

# def json_response(data, status=200):
#     """Create JSON response with proper headers"""
#     response = jsonify(data)
#     response.status_code = status
#     return response

# @app.before_request
# def session_timeout_handler():
#     """Handle session timeout"""
#     if request.endpoint in ['static']:
#         return
    
#     now = datetime.utcnow()
#     last_activity = session.get('last_activity')

#     if last_activity:
#         if isinstance(last_activity, str):
#             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
#         last_activity = last_activity.replace(tzinfo=None)

#         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
#             session.clear()
#             if is_ajax_request():
#                 return json_response({
#                     'error': 'session_expired',
#                     'message': 'Your session has expired. Please log in again.'
#                 }, 401)
#             flash('Your session has expired. Please log in again.', 'error')
#             return redirect(url_for('logInExistingUser'))

#     session['last_activity'] = now

# @app.route('/signup', methods=['GET', 'POST'])
# def signUpNewUser():
#     """Handle user registration"""
#     if request.method == 'POST':
#         data = request.form.to_dict()
        
#         # Validate password
#         is_valid_password, validations = validate_password(data.get('password', ''))
#         if not is_valid_password:
#             error_msg = {
#                 'error': 'invalid_password',
#                 'message': 'Password does not meet requirements',
#                 'validations': validations
#             }
#             if is_ajax_request():
#                 return json_response(error_msg, 400)
#             flash('Password does not meet requirements', 'error')
#             return redirect(url_for('signUpNewUser'))

#         # Check email existence
#         if Users.query.filter_by(email=data.get('email')).first():
#             error_msg = {
#                 'error': 'email_exists',
#                 'message': 'Email already exists in our records'
#             }
#             if is_ajax_request():
#                 return json_response(error_msg, 400)
#             flash('Email already registered. Please log in.', 'error')
#             return redirect(url_for('signUpNewUser'))

#         try:
#             new_user = Users(
#                 firstname=data.get('firstname'),
#                 lastname=data.get('lastname'),
#                 email=data.get('email'),
#                 password=generate_password_hash(data.get('password'))
#             )
#             db.session.add(new_user)
#             db.session.commit()
            
#             success_msg = {
#                 'message': 'Registration successful! Please log in.',
#                 'redirect': url_for('logInExistingUser')
#             }
#             if is_ajax_request():
#                 return json_response(success_msg)
#             flash('Registration successful! Please log in.', 'success')
#             return redirect(url_for('logInExistingUser'))
            
#         except Exception as e:
#             db.session.rollback()
#             error_msg = {
#                 'error': 'server_error',
#                 'message': 'An error occurred during registration'
#             }
#             if is_ajax_request():
#                 return json_response(error_msg, 500)
#             flash('An error occurred during registration', 'error')
#             return redirect(url_for('signUpNewUser'))

#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def logInExistingUser():
#     """Handle user login"""
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = Users.query.filter_by(email=email).first()

#         if user and check_password_hash(user.password, password):
#             session['userId'] = user.userId
#             session['last_activity'] = datetime.utcnow()
#             session.permanent = True

#             success_msg = {
#                 'message': 'Logged in successfully!',
#                 'redirect': url_for('loggedInHomePage')
#             }
#             if is_ajax_request():
#                 return json_response(success_msg)
#             flash('Logged in successfully!', 'success')
#             return redirect(url_for('loggedInHomePage'))
        
#         error_msg = {
#             'error': 'invalid_credentials',
#             'message': 'Incorrect email or password'
#         }
#         if is_ajax_request():
#             return json_response(error_msg, 401)
#         flash('Invalid email or password. Please try again.', 'error')
#         return redirect(url_for('logInExistingUser'))

#     return render_template('login.html')

# @app.route('/')
# def homePage():
#     """Handle home page"""
#     if 'userId' in session:
#         user = Users.query.get(session['userId'])
#         if is_ajax_request():
#             return json_response({'user': user.to_dict()})
#         return render_template('home.html', user=user)
#     return render_template('index.html')

# @app.route('/home')
# def loggedInHomePage():
#     """Handle logged-in home page"""
#     if 'userId' not in session:
#         error_msg = {
#             'error': 'unauthorized',
#             'message': 'You must be logged in to access this page'
#         }
#         if is_ajax_request():
#             return json_response(error_msg, 401)
#         flash('You must be logged in to access this page.', 'error')
#         return redirect(url_for('logInExistingUser'))

#     user = Users.query.get(session['userId'])
#     if is_ajax_request():
#         return json_response({'user': user.to_dict()})
#     return render_template('home.html', user=user)

# @app.route('/logout')
# def logout():
#     """Handle user logout"""
#     session.clear()
#     if is_ajax_request():
#         return json_response({
#             'message': 'Logged out successfully',
#             'redirect': url_for('logInExistingUser')
#         })
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('logInExistingUser'))

# @app.route('/check-email', methods=['POST'])
# def checkEmail():
#     """Check email availability"""
#     email = request.form.get('email')
#     exists = Users.query.filter_by(email=email).first() is not None
#     return json_response({'exists': exists})

# @app.route('/validate-password', methods=['POST'])
# def validatePassword():
#     """Validate password strength"""
#     password = request.form.get('password')
#     is_valid, validations = validate_password(password)
#     return json_response({
#         'valid': is_valid,
#         'validations': validations
#     })

# # Error handlers
# @app.errorhandler(404)
# def page_not_found(e):
#     """Handle 404 errors"""
#     error_msg = {
#         'error': 'not_found',
#         'message': 'Page not found'
#     }
#     if is_ajax_request():
#         return json_response(error_msg, 404)
#     if 'userId' in session:
#         user = Users.query.get(session['userId'])
#         return render_template('404.html', user=user), 404
#     return redirect(url_for('logInExistingUser'))

# @app.errorhandler(500)
# def internal_server_error(e):
#     """Handle 500 errors"""
#     error_msg = {
#         'error': 'server_error',
#         'message': 'An internal server error occurred'
#     }
#     if is_ajax_request():
#         return json_response(error_msg, 500)
#     flash('An internal server error occurred', 'error')
#     return redirect(url_for('logInExistingUser'))

# # Quiz routes
# @app.route('/playquiz')
# def quizPage():
#     """Handle quiz page"""
#     if 'userId' not in session:
#         return redirect(url_for('logInExistingUser'))
#     user = Users.query.get(session['userId'])
#     return render_template('choosequiz.html', user=user)

# @app.route('/random-quiz')
# def randomQuiz():
#     """Handle random quiz"""
#     if 'userId' not in session:
#         return redirect(url_for('logInExistingUser'))
#     user = Users.query.get(session['userId'])
#     return render_template('singlequiz.html', user=user)

# @app.route('/my-quizzes')
# def myQuizzes():
#     """Handle user's quizzes"""
#     if 'userId' not in session:
#         return redirect(url_for('logInExistingUser'))
#     user = Users.query.get(session['userId'])
#     return render_template('comingsoon.html', user=user)

# @app.route('/profile')
# def userProfile():
#     """Handle user profile"""
#     if 'userId' not in session:
#         return redirect(url_for('logInExistingUser'))
#     user = Users.query.get(session['userId'])
#     return render_template('comingsoon.html', user=user)

# @app.route('/leaderboard')
# def leaderboard():
#     """Handle leaderboard"""
#     if 'userId' not in session:
#         return redirect(url_for('logInExistingUser'))
#     user = Users.query.get(session['userId'])
#     return render_template('comingsoon.html', user=user)

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create database tables
#     port = int(environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)


from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from os import getenv, environ
from dotenv import load_dotenv
from datetime import timedelta, datetime, timezone
import re
import json

# Load environment variables
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = getenv('SECRET_KEY')
db = SQLAlchemy(app)

# Password validation patterns
PASSWORD_PATTERNS = {
    'length': r'.{8,}',
    'number': r'\d',
    'special': r'[!@#$%^&*(),.?":{}|<>]',
    'case': r'(?=.*[a-z])(?=.*[A-Z])'
}

class Users(db.Model):
    """User model for the application"""
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            'userId': self.userId,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

def validate_password(password):
    """Validate password against defined patterns"""
    validations = {
        'length': bool(re.search(PASSWORD_PATTERNS['length'], password)),
        'number': bool(re.search(PASSWORD_PATTERNS['number'], password)),
        'special': bool(re.search(PASSWORD_PATTERNS['special'], password)),
        'case': bool(re.search(PASSWORD_PATTERNS['case'], password))
    }
    return all(validations.values()), validations

def is_ajax_request():
    """Check if request is AJAX"""
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def json_response(data, status=200):
    """Create JSON response with proper headers"""
    response = jsonify(data)
    response.status_code = status
    return response

@app.before_request
def session_timeout_handler():
    """Handle session timeout"""
    if request.endpoint in ['static']:
        return
    
    now = datetime.utcnow()
    last_activity = session.get('last_activity')

    if last_activity:
        if isinstance(last_activity, str):
            last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
        last_activity = last_activity.replace(tzinfo=None)

        if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
            session.clear()
            if is_ajax_request():
                return json_response({
                    'error': 'session_expired',
                    'message': 'Your session has expired. Please log in again.'
                }, 401)
            flash('Your session has expired. Please log in again.', 'error')
            return redirect(url_for('logInExistingUser'))

    session['last_activity'] = now

@app.route('/signup', methods=['GET', 'POST'])
def signUpNewUser():
    """Handle user registration"""
    if request.method == 'POST':
        data = request.form.to_dict()
        
        # Validate password
        is_valid_password, validations = validate_password(data.get('password', ''))
        if not is_valid_password:
            error_msg = {
                'error': 'invalid_password',
                'message': 'Password does not meet requirements',
                'validations': validations
            }
            if is_ajax_request():
                return json_response(error_msg, 400)
            flash('Password does not meet requirements', 'error')
            return redirect(url_for('signUpNewUser'))

        # Check email existence
        if Users.query.filter_by(email=data.get('email')).first():
            error_msg = {
                'error': 'email_exists',
                'message': 'Email already exists in our records'
            }
            if is_ajax_request():
                return json_response(error_msg, 400)
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
            
            success_msg = {
                'message': 'Registration successful! Please log in.',
                'redirect': url_for('logInExistingUser')
            }
            if is_ajax_request():
                return json_response(success_msg)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('logInExistingUser'))
            
        except Exception as e:
            db.session.rollback()
            error_msg = {
                'error': 'server_error',
                'message': 'An error occurred during registration'
            }
            if is_ajax_request():
                return json_response(error_msg, 500)
            flash('An error occurred during registration', 'error')
            return redirect(url_for('signUpNewUser'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def logInExistingUser():
    """Handle user login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['userId'] = user.userId
            session['last_activity'] = datetime.utcnow()
            session.permanent = True

            success_msg = {
                'message': 'Logged in successfully!',
                'redirect': url_for('loggedInHomePage')
            }
            if is_ajax_request():
                return json_response(success_msg)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('loggedInHomePage'))
        
        error_msg = {
            'error': 'invalid_credentials',
            'message': 'Incorrect email or password'
        }
        if is_ajax_request():
            return json_response(error_msg, 401)
        flash('Invalid email or password. Please try again.', 'error')
        return redirect(url_for('logInExistingUser'))

    return render_template('login.html')

@app.route('/')
def homePage():
    """Handle home page"""
    if 'userId' in session:
        user = Users.query.get(session['userId'])
        if is_ajax_request():
            return json_response({'user': user.to_dict()})
        return render_template('home.html', user=user)
    return render_template('index.html')

@app.route('/home')
def loggedInHomePage():
    """Handle logged-in home page"""
    if 'userId' not in session:
        error_msg = {
            'error': 'unauthorized',
            'message': 'You must be logged in to access this page'
        }
        if is_ajax_request():
            return json_response(error_msg, 401)
        flash('You must be logged in to access this page.', 'error')
        return redirect(url_for('logInExistingUser'))

    user = Users.query.get(session['userId'])
    if is_ajax_request():
        return json_response({'user': user.to_dict()})
    return render_template('home.html', user=user)

@app.route('/logout')
def logout():
    """Handle user logout"""
    session.clear()
    if is_ajax_request():
        return json_response({
            'message': 'Logged out successfully',
            'redirect': url_for('logInExistingUser')
        })
    flash('You have been logged out.', 'info')
    return redirect(url_for('logInExistingUser'))

@app.route('/check-email', methods=['POST'])
def checkEmail():
    """Check email availability"""
    email = request.form.get('email')
    exists = Users.query.filter_by(email=email).first() is not None
    return json_response({'exists': exists})

@app.route('/validate-password', methods=['POST'])
def validatePassword():
    """Validate password strength"""
    password = request.form.get('password')
    is_valid, validations = validate_password(password)
    return json_response({
        'valid': is_valid,
        'validations': validations
    })

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    error_msg = {
        'error': 'not_found',
        'message': 'Page not found'
    }
    if is_ajax_request():
        return json_response(error_msg, 404)
    if 'userId' in session:
        user = Users.query.get(session['userId'])
        return render_template('404.html', user=user), 404
    return redirect(url_for('logInExistingUser'))

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors"""
    error_msg = {
        'error': 'server_error',
        'message': 'An internal server error occurred'
    }
    if is_ajax_request():
        return json_response(error_msg, 500)
    flash('An internal server error occurred', 'error')
    return redirect(url_for('logInExistingUser'))

# Quiz routes
@app.route('/playquiz')
def quizPage():
    """Handle quiz page"""
    if 'userId' not in session:
        return redirect(url_for('logInExistingUser'))
    user = Users.query.get(session['userId'])
    return render_template('choosequiz.html', user=user)

@app.route('/random-quiz')
def randomQuiz():
    """Handle random quiz"""
    if 'userId' not in session:
        return redirect(url_for('logInExistingUser'))
    user = Users.query.get(session['userId'])
    return render_template('singlequiz.html', user=user)

@app.route('/my-quizzes')
def myQuizzes():
    """Handle user's quizzes"""
    if 'userId' not in session:
        return redirect(url_for('logInExistingUser'))
    user = Users.query.get(session['userId'])
    return render_template('comingsoon.html', user=user)

@app.route('/profile')
def userProfile():
    """Handle user profile"""
    if 'userId' not in session:
        return redirect(url_for('logInExistingUser'))
    user = Users.query.get(session['userId'])
    return render_template('comingsoon.html', user=user)

@app.route('/leaderboard')
def leaderboard():
    """Handle leaderboard"""
    if 'userId' not in session:
        return redirect(url_for('logInExistingUser'))
    user = Users.query.get(session['userId'])
    return render_template('comingsoon.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
