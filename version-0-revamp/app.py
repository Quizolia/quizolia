# # # # from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
# # # # from flask_sqlalchemy import SQLAlchemy
# # # # from werkzeug.security import generate_password_hash, check_password_hash
# # # # from os import getenv, environ
# # # # from dotenv import load_dotenv
# # # # from datetime import timedelta, datetime, timezone
# # # # import re

# # # # # Load the environment variables
# # # # load_dotenv()
# # # # app = Flask(__name__)
# # # # app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
# # # # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# # # # app.secret_key = getenv('SECRET_KEY')
# # # # db = SQLAlchemy(app)


# # # # # Password validation regex patterns
# # # # PASSWORD_PATTERNS = {
# # # #     'length': r'.{8,}',
# # # #     'number': r'\d',
# # # #     'special': r'[!@#$%^&*(),.?":{}|<>]',
# # # #     'case': r'(?=.*[a-z])(?=.*[A-Z])'
# # # # }


# # # # class Users(db.Model):
# # # #     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
# # # #     firstname = db.Column(db.String(50), nullable=False)
# # # #     lastname = db.Column(db.String(50), nullable=False)
# # # #     email = db.Column(db.String(100), nullable=False, unique=True)
# # # #     password = db.Column(db.String(100), nullable=False)


# # # # def validate_password(password):
# # # #     """Validate password against defined patterns"""
# # # #     return all(
# # # #         bool(re.search(pattern, password))
# # # #         for pattern in PASSWORD_PATTERNS.values()
# # # #     )


# # # # def is_ajax_request():
# # # #     """Check if the request is an AJAX request"""
# # # #     return request.headers.get('X-Requested-With') == 'XMLHttpRequest'


# # # # @app.before_request
# # # # def session_timeout_handler():
# # # #     if request.endpoint in ['static']:
# # # #         return

# # # #     now = datetime.utcnow()
# # # #     last_activity = session.get('last_activity')

# # # #     if last_activity:
# # # #         if isinstance(last_activity, str):
# # # #             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
# # # #         last_activity = last_activity.replace(tzinfo=None)

# # # #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# # # #             session.pop('userId', None)
# # # #             session.pop('last_activity', None)
# # # #             if is_ajax_request():
# # # #                 return jsonify({'error': 'session_expired', 'message': 'Your session has expired. Please log in again.'}), 401
# # # #             flash('Your session has expired. Please log in again.', 'error')
# # # #             return redirect('/login')

# # # #     session['last_activity'] = now


# # # # @app.route('/signup', methods=['GET', 'POST'])
# # # # def signUpNewUser():
# # # #     if request.method == 'POST':
# # # #         UserFirstName = request.form['firstname']
# # # #         UserLastName = request.form['lastname']
# # # #         UserEmail = request.form['email']
# # # #         UserPassword = request.form['password']

# # # #         # Validate password
# # # #         if not validate_password(UserPassword):
# # # #             if is_ajax_request():
# # # #                 return jsonify({
# # # #                     'error': 'invalid_password',
# # # #                     'message': 'Password does not meet requirements'
# # # #                 }), 400
# # # #             flash('Password does not meet requirements', 'error')
# # # #             return redirect('/signup')

# # # #         # Check if email exists
# # # #         if Users.query.filter_by(email=UserEmail).first():
# # # #             if is_ajax_request():
# # # #                 return jsonify({
# # # #                     'error': 'email_exists',
# # # #                     'message': 'Email already exists in our records'
# # # #                 }), 400
# # # #             flash('Email already registered. Please log in.', 'error')
# # # #             return redirect('/signup')

# # # #         try:
# # # #             hashed_password = generate_password_hash(UserPassword)
# # # #             new_user = Users(
# # # #                 firstname=UserFirstName,
# # # #                 lastname=UserLastName,
# # # #                 email=UserEmail,
# # # #                 password=hashed_password
# # # #             )
# # # #             db.session.add(new_user)
# # # #             db.session.commit()

# # # #             if is_ajax_request():
# # # #                 return jsonify({
# # # #                     'message': 'Registration successful! Please log in.',
# # # #                     'redirect': '/login'
# # # #                 }), 200
# # # #             flash('Registration successful! Please log in.', 'success')
# # # #             return redirect('/login')
# # # #         except Exception as e:
# # # #             db.session.rollback()
# # # #             if is_ajax_request():
# # # #                 return jsonify({
# # # #                     'error': 'server_error',
# # # #                     'message': 'An error occurred during registration'
# # # #                 }), 500
# # # #             flash('An error occurred during registration', 'error')
# # # #             return redirect('/signup')

# # # #     return render_template('signup.html')


# # # # @app.route('/login', methods=['GET', 'POST'])
# # # # def logInExistingUser():
# # # #     if request.method == 'POST':
# # # #         email = request.form['email']
# # # #         password = request.form['password']
# # # #         user = Users.query.filter_by(email=email).first()

# # # #         if user and check_password_hash(user.password, password):
# # # #             session['userId'] = user.userId
# # # #             session['last_activity'] = datetime.utcnow()
# # # #             session.permanent = True

# # # #             if is_ajax_request():
# # # #                 return jsonify({
# # # #                     'message': 'Logged in successfully!',
# # # #                     'redirect': '/home'
# # # #                 }), 200
# # # #             flash('Logged in successfully!', 'success')
# # # #             return redirect('/home')

# # # #         if is_ajax_request():
# # # #             return jsonify({
# # # #                 'error': 'invalid_credentials',
# # # #                 'message': 'Incorrect email or password'
# # # #             }), 401
# # # #         flash('Invalid email or password. Please try again.', 'error')
# # # #         return redirect('/login')


# # # #     return render_template('login.html')

# # # # # The rest of your routes remain the same, but you might want to add AJAX handling
# # # # # to them as well if needed


# # # # @app.errorhandler(404)
# # # # def page_not_found(e):
# # # #     if is_ajax_request():
# # # #         return jsonify({'error': 'not_found', 'message': 'Page not found'}), 404
# # # #     if 'userId' in session:
# # # #         user = Users.query.get(session['userId'])
# # # #         return render_template('404.html', user=user), 404
# # # #     return redirect('/login')


# # # # @app.errorhandler(500)
# # # # def internal_error(e):
# # # #     if is_ajax_request():
# # # #         return jsonify({'error': 'server_error', 'message': 'An internal error occurred'}), 500
# # # #     flash('An internal error occurred', 'error')
# # # #     return redirect('/login')


# # # # if __name__ == '__main__':
# # # #     port = int(environ.get("PORT", 5000))
# # # #     app.run(host="0.0.0.0", port=port)


# # # from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
# # # from flask_sqlalchemy import SQLAlchemy
# # # from werkzeug.security import generate_password_hash, check_password_hash
# # # from os import getenv, environ
# # # from dotenv import load_dotenv
# # # from datetime import timedelta, datetime, timezone
# # # import re
# # # import json

# # # # Load environment variables
# # # load_dotenv()
# # # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
# # # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # # app.secret_key = getenv('SECRET_KEY')
# # # db = SQLAlchemy(app)

# # # # Password validation patterns
# # # PASSWORD_PATTERNS = {
# # #     'length': r'.{8,}',
# # #     'number': r'\d',
# # #     'special': r'[!@#$%^&*(),.?":{}|<>]',
# # #     'case': r'(?=.*[a-z])(?=.*[A-Z])'
# # # }

# # # class Users(db.Model):
# # #     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
# # #     firstname = db.Column(db.String(50), nullable=False)
# # #     lastname = db.Column(db.String(50), nullable=False)
# # #     email = db.Column(db.String(100), nullable=False, unique=True)
# # #     password = db.Column(db.String(100), nullable=False)
# # #     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
# # #     def to_dict(self):
# # #         return {
# # #             'userId': self.userId,
# # #             'firstname': self.firstname,
# # #             'lastname': self.lastname,
# # #             'email': self.email,
# # #             'created_at': self.created_at.isoformat()
# # #         }

# # # def validate_password(password):
# # #     """Validate password against defined patterns"""
# # #     validations = {
# # #         'length': bool(re.search(PASSWORD_PATTERNS['length'], password)),
# # #         'number': bool(re.search(PASSWORD_PATTERNS['number'], password)),
# # #         'special': bool(re.search(PASSWORD_PATTERNS['special'], password)),
# # #         'case': bool(re.search(PASSWORD_PATTERNS['case'], password))
# # #     }
# # #     return all(validations.values()), validations

# # # def is_ajax_request():
# # #     """Check if request is AJAX"""
# # #     return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

# # # def json_response(data, status=200):
# # #     """Create JSON response with proper headers"""
# # #     response = jsonify(data)
# # #     response.status_code = status
# # #     return response

# # # @app.before_request
# # # def session_timeout_handler():
# # #     """Handle session timeout"""
# # #     if request.endpoint in ['static']:
# # #         return
    
# # #     now = datetime.utcnow()
# # #     last_activity = session.get('last_activity')

# # #     if last_activity:
# # #         if isinstance(last_activity, str):
# # #             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
# # #         last_activity = last_activity.replace(tzinfo=None)

# # #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# # #             session.clear()
# # #             if is_ajax_request():
# # #                 return json_response({
# # #                     'error': 'session_expired',
# # #                     'message': 'Your session has expired. Please log in again.'
# # #                 }, 401)
# # #             flash('Your session has expired. Please log in again.', 'error')
# # #             return redirect(url_for('logInExistingUser'))

# # #     session['last_activity'] = now

# # # @app.route('/signup', methods=['GET', 'POST'])
# # # def signUpNewUser():
# # #     """Handle user registration"""
# # #     if request.method == 'POST':
# # #         data = request.form.to_dict()
        
# # #         # Validate password
# # #         is_valid_password, validations = validate_password(data.get('password', ''))
# # #         if not is_valid_password:
# # #             error_msg = {
# # #                 'error': 'invalid_password',
# # #                 'message': 'Password does not meet requirements',
# # #                 'validations': validations
# # #             }
# # #             if is_ajax_request():
# # #                 return json_response(error_msg, 400)
# # #             flash('Password does not meet requirements', 'error')
# # #             return redirect(url_for('signUpNewUser'))

# # #         # Check email existence
# # #         if Users.query.filter_by(email=data.get('email')).first():
# # #             error_msg = {
# # #                 'error': 'email_exists',
# # #                 'message': 'Email already exists in our records'
# # #             }
# # #             if is_ajax_request():
# # #                 return json_response(error_msg, 400)
# # #             flash('Email already registered. Please log in.', 'error')
# # #             return redirect(url_for('signUpNewUser'))

# # #         try:
# # #             new_user = Users(
# # #                 firstname=data.get('firstname'),
# # #                 lastname=data.get('lastname'),
# # #                 email=data.get('email'),
# # #                 password=generate_password_hash(data.get('password'))
# # #             )
# # #             db.session.add(new_user)
# # #             db.session.commit()
            
# # #             success_msg = {
# # #                 'message': 'Registration successful! Please log in.',
# # #                 'redirect': url_for('logInExistingUser')
# # #             }
# # #             if is_ajax_request():
# # #                 return json_response(success_msg)
# # #             flash('Registration successful! Please log in.', 'success')
# # #             return redirect(url_for('logInExistingUser'))
            
# # #         except Exception as e:
# # #             db.session.rollback()
# # #             error_msg = {
# # #                 'error': 'server_error',
# # #                 'message': 'An error occurred during registration'
# # #             }
# # #             if is_ajax_request():
# # #                 return json_response(error_msg, 500)
# # #             flash('An error occurred during registration', 'error')
# # #             return redirect(url_for('signUpNewUser'))

# # #     return render_template('signup.html')

# # # @app.route('/login', methods=['GET', 'POST'])
# # # def logInExistingUser():
# # #     """Handle user login"""
# # #     if request.method == 'POST':
# # #         email = request.form.get('email')
# # #         password = request.form.get('password')
# # #         user = Users.query.filter_by(email=email).first()

# # #         if user and check_password_hash(user.password, password):
# # #             session['userId'] = user.userId
# # #             session['last_activity'] = datetime.utcnow()
# # #             session.permanent = True

# # #             success_msg = {
# # #                 'message': 'Logged in successfully!',
# # #                 'redirect': url_for('loggedInHomePage')
# # #             }
# # #             if is_ajax_request():
# # #                 return json_response(success_msg)
# # #             flash('Logged in successfully!', 'success')
# # #             return redirect(url_for('loggedInHomePage'))
        
# # #         error_msg = {
# # #             'error': 'invalid_credentials',
# # #             'message': 'Incorrect email or password'
# # #         }
# # #         if is_ajax_request():
# # #             return json_response(error_msg, 401)
# # #         flash('Invalid email or password. Please try again.', 'error')
# # #         return redirect(url_for('logInExistingUser'))

# # #     return render_template('login.html')

# # # @app.route('/')
# # # def homePage():
# # #     """Handle home page"""
# # #     if 'userId' in session:
# # #         user = Users.query.get(session['userId'])
# # #         if is_ajax_request():
# # #             return json_response({'user': user.to_dict()})
# # #         return render_template('home.html', user=user)
# # #     return render_template('index.html')

# # # @app.route('/home')
# # # def loggedInHomePage():
# # #     """Handle logged-in home page"""
# # #     if 'userId' not in session:
# # #         error_msg = {
# # #             'error': 'unauthorized',
# # #             'message': 'You must be logged in to access this page'
# # #         }
# # #         if is_ajax_request():
# # #             return json_response(error_msg, 401)
# # #         flash('You must be logged in to access this page.', 'error')
# # #         return redirect(url_for('logInExistingUser'))

# # #     user = Users.query.get(session['userId'])
# # #     if is_ajax_request():
# # #         return json_response({'user': user.to_dict()})
# # #     return render_template('home.html', user=user)

# # # @app.route('/logout')
# # # def logout():
# # #     """Handle user logout"""
# # #     session.clear()
# # #     if is_ajax_request():
# # #         return json_response({
# # #             'message': 'Logged out successfully',
# # #             'redirect': url_for('logInExistingUser')
# # #         })
# # #     flash('You have been logged out.', 'info')
# # #     return redirect(url_for('logInExistingUser'))

# # # @app.route('/check-email', methods=['POST'])
# # # def checkEmail():
# # #     """Check email availability"""
# # #     email = request.form.get('email')
# # #     exists = Users.query.filter_by(email=email).first() is not None
# # #     return json_response({'exists': exists})

# # # @app.route('/validate-password', methods=['POST'])
# # # def validatePassword():
# # #     """Validate password strength"""
# # #     password = request.form.get('password')
# # #     is_valid, validations = validate_password(password)
# # #     return json_response({
# # #         'valid': is_valid,
# # #         'validations': validations
# # #     })

# # # # Error handlers
# # # @app.errorhandler(404)
# # # def page_not_found(e):
# # #     """Handle 404 errors"""
# # #     error_msg = {
# # #         'error': 'not_found',
# # #         'message': 'Page not found'
# # #     }
# # #     if is_ajax_request():
# # #         return json_response(error_msg, 404)
# # #     if 'userId' in session:
# # #         user = Users.query.get(session['userId'])
# # #         return render_template('404.html', user=user), 404
# # #     return redirect(url_for('logInExistingUser'))

# # # @app.errorhandler(500)
# # # def internal_server_error(e):
# # #     """Handle 500 errors"""
# # #     error_msg = {
# # #         'error': 'server_error',
# # #         'message': 'An internal server error occurred'
# # #     }
# # #     if is_ajax_request():
# # #         return json_response(error_msg, 500)
# # #     flash('An internal server error occurred', 'error')
# # #     return redirect(url_for('logInExistingUser'))

# # # # Quiz routes
# # # @app.route('/playquiz')
# # # def quizPage():
# # #     """Handle quiz page"""
# # #     if 'userId' not in session:
# # #         return redirect(url_for('logInExistingUser'))
# # #     user = Users.query.get(session['userId'])
# # #     return render_template('choosequiz.html', user=user)

# # # @app.route('/random-quiz')
# # # def randomQuiz():
# # #     """Handle random quiz"""
# # #     if 'userId' not in session:
# # #         return redirect(url_for('logInExistingUser'))
# # #     user = Users.query.get(session['userId'])
# # #     return render_template('singlequiz.html', user=user)

# # # @app.route('/my-quizzes')
# # # def myQuizzes():
# # #     """Handle user's quizzes"""
# # #     if 'userId' not in session:
# # #         return redirect(url_for('logInExistingUser'))
# # #     user = Users.query.get(session['userId'])
# # #     return render_template('comingsoon.html', user=user)

# # # @app.route('/profile')
# # # def userProfile():
# # #     """Handle user profile"""
# # #     if 'userId' not in session:
# # #         return redirect(url_for('logInExistingUser'))
# # #     user = Users.query.get(session['userId'])
# # #     return render_template('comingsoon.html', user=user)

# # # @app.route('/leaderboard')
# # # def leaderboard():
# # #     """Handle leaderboard"""
# # #     if 'userId' not in session:
# # #         return redirect(url_for('logInExistingUser'))
# # #     user = Users.query.get(session['userId'])
# # #     return render_template('comingsoon.html', user=user)

# # # if __name__ == '__main__':
# # #     with app.app_context():
# # #         db.create_all()  # Create database tables
# # #     port = int(environ.get("PORT", 5000))
# # #     app.run(host="0.0.0.0", port=port)


# # from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
# # from flask_sqlalchemy import SQLAlchemy
# # from werkzeug.security import generate_password_hash, check_password_hash
# # from os import getenv, environ
# # from dotenv import load_dotenv
# # from datetime import timedelta, datetime, timezone
# # import re
# # import json

# # # Load environment variables
# # load_dotenv()
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
# # app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.secret_key = getenv('SECRET_KEY')
# # db = SQLAlchemy(app)

# # # Password validation patterns
# # PASSWORD_PATTERNS = {
# #     'length': r'.{8,}',
# #     'number': r'\d',
# #     'special': r'[!@#$%^&*(),.?":{}|<>]',
# #     'case': r'(?=.*[a-z])(?=.*[A-Z])'
# # }

# # # class Users(db.Model):
# # #     """User model for the application"""
# # #     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
# # #     firstname = db.Column(db.String(50), nullable=False)
# # #     lastname = db.Column(db.String(50), nullable=False)
# # #     email = db.Column(db.String(100), nullable=False, unique=True)
# # #     password = db.Column(db.String(255), nullable=False)
# # #     created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

# # #     def to_dict(self):
# # #         """Convert user object to dictionary"""
# # #         return {
# # #             'userId': self.userId,
# # #             'firstname': self.firstname,
# # #             'lastname': self.lastname,
# # #             'email': self.email,
# # #             'created_at': self.created_at.isoformat() if self.created_at else None
# # #         }


# # class Users(db.Model):
# #     """User model for the application"""
# #     __tablename__ = 'users'
# #     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     firstname = db.Column(db.String(50), nullable=False)
# #     lastname = db.Column(db.String(50), nullable=False)
# #     email = db.Column(db.String(100), nullable=False, unique=True)
# #     password = db.Column(db.String(255), nullable=False)
# #     created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

# #     def to_dict(self):
# #         """Convert user object to dictionary"""
# #         return {
# #             'userId': self.userId,
# #             'firstname': self.firstname,
# #             'lastname': self.lastname,
# #             'email': self.email,
# #             'created_at': self.created_at.isoformat() if self.created_at else None
# #         }


# # def validate_password(password):
# #     """Validate password against defined patterns"""
# #     validations = {
# #         'length': bool(re.search(PASSWORD_PATTERNS['length'], password)),
# #         'number': bool(re.search(PASSWORD_PATTERNS['number'], password)),
# #         'special': bool(re.search(PASSWORD_PATTERNS['special'], password)),
# #         'case': bool(re.search(PASSWORD_PATTERNS['case'], password))
# #     }
# #     return all(validations.values()), validations

# # def is_ajax_request():
# #     """Check if request is AJAX"""
# #     return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

# # def json_response(data, status=200):
# #     """Create JSON response with proper headers"""
# #     response = jsonify(data)
# #     response.status_code = status
# #     return response

# # @app.before_request
# # def session_timeout_handler():
# #     """Handle session timeout"""
# #     if request.endpoint in ['static']:
# #         return
    
# #     now = datetime.utcnow()
# #     last_activity = session.get('last_activity')

# #     if last_activity:
# #         if isinstance(last_activity, str):
# #             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
# #         last_activity = last_activity.replace(tzinfo=None)

# #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# #             session.clear()
# #             if is_ajax_request():
# #                 return json_response({
# #                     'error': 'session_expired',
# #                     'message': 'Your session has expired. Please log in again.'
# #                 }, 401)
# #             flash('Your session has expired. Please log in again.', 'error')
# #             return redirect(url_for('logInExistingUser'))

# #     session['last_activity'] = now

# # @app.route('/signup', methods=['GET', 'POST'])
# # def signUpNewUser():
# #     """Handle user registration"""
# #     if request.method == 'POST':
# #         data = request.form.to_dict()
        
# #         # Validate password
# #         is_valid_password, validations = validate_password(data.get('password', ''))
# #         if not is_valid_password:
# #             error_msg = {
# #                 'error': 'invalid_password',
# #                 'message': 'Password does not meet requirements',
# #                 'validations': validations
# #             }
# #             if is_ajax_request():
# #                 return json_response(error_msg, 400)
# #             flash('Password does not meet requirements', 'error')
# #             return redirect(url_for('signUpNewUser'))

# #         # Check email existence
# #         if Users.query.filter_by(email=data.get('email')).first():
# #             error_msg = {
# #                 'error': 'email_exists',
# #                 'message': 'Email already exists in our records'
# #             }
# #             if is_ajax_request():
# #                 return json_response(error_msg, 400)
# #             flash('Email already registered. Please log in.', 'error')
# #             return redirect(url_for('signUpNewUser'))

# #         try:
# #             new_user = Users(
# #                 firstname=data.get('firstname'),
# #                 lastname=data.get('lastname'),
# #                 email=data.get('email'),
# #                 password=generate_password_hash(data.get('password'))
# #             )
# #             db.session.add(new_user)
# #             db.session.commit()
            
# #             success_msg = {
# #                 'message': 'Registration successful! Please log in.',
# #                 'redirect': url_for('logInExistingUser')
# #             }
# #             if is_ajax_request():
# #                 return json_response(success_msg)
# #             flash('Registration successful! Please log in.', 'success')
# #             return redirect(url_for('logInExistingUser'))
            
# #         except Exception as e:
# #             db.session.rollback()
# #             error_msg = {
# #                 'error': 'server_error',
# #                 'message': 'An error occurred during registration'
# #             }
# #             if is_ajax_request():
# #                 return json_response(error_msg, 500)
# #             flash('An error occurred during registration', 'error')
# #             return redirect(url_for('signUpNewUser'))

# #     return render_template('signup.html')

# # @app.route('/login', methods=['GET', 'POST'])
# # def logInExistingUser():
# #     """Handle user login"""
# #     if request.method == 'POST':
# #         email = request.form.get('email')
# #         password = request.form.get('password')
# #         user = Users.query.filter_by(email=email).first()

# #         if user and check_password_hash(user.password, password):
# #             session['userId'] = user.userId
# #             session['last_activity'] = datetime.utcnow()
# #             session.permanent = True

# #             success_msg = {
# #                 'message': 'Logged in successfully!',
# #                 'redirect': url_for('loggedInHomePage')
# #             }
# #             if is_ajax_request():
# #                 return json_response(success_msg)
# #             flash('Logged in successfully!', 'success')
# #             return redirect(url_for('loggedInHomePage'))
        
# #         error_msg = {
# #             'error': 'invalid_credentials',
# #             'message': 'Incorrect email or password'
# #         }
# #         if is_ajax_request():
# #             return json_response(error_msg, 401)
# #         flash('Invalid email or password. Please try again.', 'error')
# #         return redirect(url_for('logInExistingUser'))

# #     return render_template('login.html')

# # @app.route('/')
# # def homePage():
# #     """Handle home page"""
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         if is_ajax_request():
# #             return json_response({'user': user.to_dict()})
# #         return render_template('home.html', user=user)
# #     return render_template('index.html')

# # @app.route('/home')
# # def loggedInHomePage():
# #     """Handle logged-in home page"""
# #     if 'userId' not in session:
# #         error_msg = {
# #             'error': 'unauthorized',
# #             'message': 'You must be logged in to access this page'
# #         }
# #         if is_ajax_request():
# #             return json_response(error_msg, 401)
# #         flash('You must be logged in to access this page.', 'error')
# #         return redirect(url_for('logInExistingUser'))

# #     user = Users.query.get(session['userId'])
# #     if is_ajax_request():
# #         return json_response({'user': user.to_dict()})
# #     return render_template('home.html', user=user)

# # @app.route('/logout')
# # def logout():
# #     """Handle user logout"""
# #     session.clear()
# #     if is_ajax_request():
# #         return json_response({
# #             'message': 'Logged out successfully',
# #             'redirect': url_for('logInExistingUser')
# #         })
# #     flash('You have been logged out.', 'info')
# #     return redirect(url_for('logInExistingUser'))

# # @app.route('/check-email', methods=['POST'])
# # def checkEmail():
# #     """Check email availability"""
# #     email = request.form.get('email')
# #     exists = Users.query.filter_by(email=email).first() is not None
# #     return json_response({'exists': exists})

# # @app.route('/validate-password', methods=['POST'])
# # def validatePassword():
# #     """Validate password strength"""
# #     password = request.form.get('password')
# #     is_valid, validations = validate_password(password)
# #     return json_response({
# #         'valid': is_valid,
# #         'validations': validations
# #     })

# # # Error handlers
# # @app.errorhandler(404)
# # def page_not_found(e):
# #     """Handle 404 errors"""
# #     error_msg = {
# #         'error': 'not_found',
# #         'message': 'Page not found'
# #     }
# #     if is_ajax_request():
# #         return json_response(error_msg, 404)
# #     if 'userId' in session:
# #         user = Users.query.get(session['userId'])
# #         return render_template('404.html', user=user), 404
# #     return redirect(url_for('logInExistingUser'))

# # @app.errorhandler(500)
# # def internal_server_error(e):
# #     """Handle 500 errors"""
# #     error_msg = {
# #         'error': 'server_error',
# #         'message': 'An internal server error occurred'
# #     }
# #     if is_ajax_request():
# #         return json_response(error_msg, 500)
# #     flash('An internal server error occurred', 'error')
# #     return redirect(url_for('logInExistingUser'))

# # # Quiz routes
# # @app.route('/playquiz')
# # def quizPage():
# #     """Handle quiz page"""
# #     if 'userId' not in session:
# #         return redirect(url_for('logInExistingUser'))
# #     user = Users.query.get(session['userId'])
# #     return render_template('choosequiz.html', user=user)

# # @app.route('/random-quiz')
# # def randomQuiz():
# #     """Handle random quiz"""
# #     if 'userId' not in session:
# #         return redirect(url_for('logInExistingUser'))
# #     user = Users.query.get(session['userId'])
# #     return render_template('singlequiz.html', user=user)

# # @app.route('/my-quizzes')
# # def myQuizzes():
# #     """Handle user's quizzes"""
# #     if 'userId' not in session:
# #         return redirect(url_for('logInExistingUser'))
# #     user = Users.query.get(session['userId'])
# #     return render_template('comingsoon.html', user=user)

# # @app.route('/profile')
# # def userProfile():
# #     """Handle user profile"""
# #     if 'userId' not in session:
# #         return redirect(url_for('logInExistingUser'))
# #     user = Users.query.get(session['userId'])
# #     return render_template('comingsoon.html', user=user)

# # @app.route('/leaderboard')
# # def leaderboard():
# #     """Handle leaderboard"""
# #     if 'userId' not in session:
# #         return redirect(url_for('logInExistingUser'))
# #     user = Users.query.get(session['userId'])
# #     return render_template('comingsoon.html', user=user)

# # if __name__ == '__main__':
# #     with app.app_context():
# #         db.create_all()  # Create database tables
# #     port = int(environ.get("PORT", 5000))
# #     app.run(host="0.0.0.0", port=port)


# from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# from os import getenv, environ
# from dotenv import load_dotenv
# from datetime import timedelta, datetime
# import re

# # Load environment variables
# load_dotenv()
# app = Flask(__name__)

# # Flask configurations
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = getenv('SECRET_KEY')

# # Initialize database
# db = SQLAlchemy(app)

# # Password validation patterns
# PASSWORD_PATTERNS = {
#     'length': r'.{8,}',               # At least 8 characters
#     'number': r'\d',                  # At least one digit
#     'special': r'[!@#$%^&*(),.?":{}|<>]',  # At least one special character
#     'case': r'(?=.*[a-z])(?=.*[A-Z])' # At least one uppercase and one lowercase letter
# }

# # Models
# class Users(db.Model):
#     """User model for the application."""
#     __tablename__ = 'users'
#     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     firstname = db.Column(db.String(50), nullable=False)
#     lastname = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

#     def to_dict(self):
#         """Convert user object to dictionary for JSON responses."""
#         return {
#             'userId': self.userId,
#             'firstname': self.firstname,
#             'lastname': self.lastname,
#             'email': self.email,
#             'created_at': self.created_at.isoformat() if self.created_at else None
#         }

# # Utility functions
# def validate_password(password):
#     """Validate password against defined patterns."""
#     validations = {
#         'length': bool(re.search(PASSWORD_PATTERNS['length'], password)),
#         'number': bool(re.search(PASSWORD_PATTERNS['number'], password)),
#         'special': bool(re.search(PASSWORD_PATTERNS['special'], password)),
#         'case': bool(re.search(PASSWORD_PATTERNS['case'], password))
#     }
#     return all(validations.values()), validations

# def is_ajax_request():
#     """Check if the request is AJAX."""
#     return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

# def json_response(data, status=200):
#     """Create a JSON response with the proper status."""
#     response = jsonify(data)
#     response.status_code = status
#     return response

# # Middleware
# # @app.before_request
# # def session_timeout_handler():
# #     """Handle session timeout."""
# #     if request.endpoint in ['static']:
# #         return

# #     now = datetime.utcnow()
# #     last_activity = session.get('last_activity')

# #     if last_activity:
# #         last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")
# #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# #             session.clear()
# #             if is_ajax_request():
# #                 return json_response({'error': 'session_expired', 'message': 'Your session has expired. Please log in again.'}, 401)
# #             flash('Your session has expired. Please log in again.', 'error')
# #             return redirect(url_for('logInExistingUser'))

# #     session['last_activity'] = now
# # @app.before_request
# # def session_timeout_handler():
# #     """Handle session timeout."""
# #     if request.endpoint in ['static']:
# #         return

# #     now = datetime.utcnow()
# #     last_activity = session.get('last_activity')

# #     if last_activity:
# #         # Ensure last_activity is treated appropriately
# #         if isinstance(last_activity, str):
# #             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")

# #         # Compare last activity with the current time
# #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# #             session.clear()
# #             if is_ajax_request():
# #                 return json_response({'error': 'session_expired', 'message': 'Your session has expired. Please log in again.'}, 401)
# #             flash('Your session has expired. Please log in again.', 'error')
# #             return redirect(url_for('logInExistingUser'))

# #     # Update the session's last activity time
# #     session['last_activity'] = now
# # @app.before_request
# # def session_timeout_handler():
# #     """Handle session timeout."""
# #     if request.endpoint in ['static']:
# #         return

# #     now = datetime.now(timezone.utc)  # Use timezone-aware datetime
# #     last_activity = session.get('last_activity')

# #     if last_activity:
# #         if isinstance(last_activity, str):  # Check if it's a string
# #             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=timezone.utc)

# #         # Ensure both datetimes are timezone-aware
# #         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# #             session.clear()
# #             if is_ajax_request():
# #                 return json_response({'error': 'session_expired', 'message': 'Your session has expired. Please log in again.'}, 401)
# #             flash('Your session has expired. Please log in again.', 'error')
# #             return redirect(url_for('logInExistingUser'))

# #     # Update session last activity as timezone-aware
# #     session['last_activity'] = now.isoformat()
# # @app.before_request
# # def session_timeout_handler():
# #     """Handle session timeout."""
# #     if request.endpoint in ['static']:
# #         return

# #     try:
# #         now = datetime.now(timezone.utc)  # Use timezone-aware datetime
# #         print(f"Current Time (now): {now}")  # Debugging log

# #         last_activity = session.get('last_activity')
# #         print(f"Last Activity from Session: {last_activity}")  # Debugging log

# #         if last_activity:
# #             if isinstance(last_activity, str):  # Check if it's a string
# #                 last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=timezone.utc)
# #                 print(f"Parsed Last Activity (timezone-aware): {last_activity}")  # Debugging log

# #             # Ensure both datetimes are timezone-aware
# #             time_difference = (now - last_activity).total_seconds()
# #             print(f"Time Difference: {time_difference} seconds")  # Debugging log

# #             if time_difference > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
# #                 session.clear()
# #                 if is_ajax_request():
# #                     return json_response({'error': 'session_expired', 'message': 'Your session has expired. Please log in again.'}, 401)
# #                 flash('Your session has expired. Please log in again.', 'error')
# #                 return redirect(url_for('logInExistingUser'))

# #         # Update session last activity as timezone-aware
# #         session['last_activity'] = now.isoformat()
# #         print(f"Updated Last Activity in Session: {session['last_activity']}")  # Debugging log

# #     except Exception as e:
# #         print(f"Error in session_timeout_handler: {e}")  # Log any unexpected error
# #         if is_ajax_request():
# #             return json_response({'error': 'server_error', 'message': 'Internal server error'}, 500)
# #         flash('An internal server error occurred. Please try again later.', 'error')
# #         return redirect(url_for('logInExistingUser'))
# @app.before_request
# def session_timeout_handler():
#     """Handle session timeout."""
#     if request.endpoint in ['static']:
#         return

#     now = datetime.utcnow()
#     last_activity = session.get('last_activity')

#     if last_activity:
#         if isinstance(last_activity, str):
#             last_activity = datetime.strptime(last_activity, "%Y-%m-%d %H:%M:%S.%f")

#         if (now - last_activity).total_seconds() > app.config['PERMANENT_SESSION_LIFETIME'].total_seconds():
#             session.clear()
#             flash('Your session has expired. Please log in again.', 'error')
#             return redirect(url_for('logInExistingUser'))

#     session['last_activity'] = now


# # Routes
# @app.route('/signup', methods=['GET', 'POST'])
# def signUpNewUser():
#     """Handle user registration."""
#     if request.method == 'POST':
#         data = request.form.to_dict()
        
#         # Validate password
#         is_valid_password, validations = validate_password(data.get('password', ''))
#         if not is_valid_password:
#             flash('Password does not meet requirements.', 'error')
#             return redirect(url_for('signUpNewUser'))

#         # Check if email already exists
#         if Users.query.filter_by(email=data.get('email')).first():
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
#             flash('Registration successful! Please log in.', 'success')
#             return redirect(url_for('logInExistingUser'))
#         except Exception as e:
#             db.session.rollback()
#             app.logger.error(f"Error during signup: {e}")
#             flash('An error occurred during registration. Please try again later.', 'error')
#             return redirect(url_for('signUpNewUser'))

#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def logInExistingUser():
#     """Handle user login."""
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = Users.query.filter_by(email=email).first()

#         if user and check_password_hash(user.password, password):
#             session['userId'] = user.userId
#             session['last_activity'] = datetime.utcnow()
#             session.permanent = True
#             flash('Logged in successfully!', 'success')
#             return redirect(url_for('loggedInHomePage'))
        
#         flash('Invalid email or password. Please try again.', 'error')
#         return redirect(url_for('logInExistingUser'))

#     return render_template('login.html')

# @app.route('/')
# def homePage():
#     """Handle the home page."""
#     if 'userId' in session:
#         user = Users.query.get(session['userId'])
#         return render_template('home.html', user=user)
#     return render_template('index.html')

# @app.route('/logout')
# def logout():
#     """Handle user logout."""
#     session.clear()
#     flash('You have been logged out.', 'info')
#     return redirect(url_for('logInExistingUser'))

# # Quiz routes (placeholders for now)
# @app.route('/playquiz')
# def quizPage():
#     """Quiz selection page."""
#     return render_template('choosequiz.html')

# @app.route('/random-quiz')
# def randomQuiz():
#     """Random quiz page."""
#     return render_template('singlequiz.html')

# @app.route('/profile')
# def userProfile():
#     """User profile page."""
#     return render_template('comingsoon.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     """Handle 404 errors."""
#     return render_template('404.html'), 404

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Ensure database tables are created
#     port = int(environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)


from flask import Flask, render_template, request, flash, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from os import getenv, environ
from dotenv import load_dotenv
from datetime import timedelta, datetime
import re
import logging

# Load environment variables
load_dotenv()
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

def login_required(f):
    """Decorator to require login for routes."""
    def decorated_function(*args, **kwargs):
        if 'userId' not in session:
            if is_ajax_request():
                return json_response({
                    'error': 'unauthorized',
                    'message': 'Please log in to access this page'
                }, 401)
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('logInExistingUser'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

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
    """Handle user registration."""
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
            flash('Password does not meet requirements.', 'error')
            return redirect(url_for('signUpNewUser'))

        # Check if email already exists
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
            logger.error(f"Error during signup: {str(e)}")
            error_msg = {
                'error': 'server_error',
                'message': 'An error occurred during registration'
            }
            if is_ajax_request():
                return json_response(error_msg, 500)
            flash('An error occurred during registration. Please try again.', 'error')
            return redirect(url_for('signUpNewUser'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def logInExistingUser():
    """Handle user login."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        try:
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
            
        except Exception as e:
            logger.error(f"Error during login: {str(e)}")
            error_msg = {
                'error': 'server_error',
                'message': 'An error occurred during login'
            }
            if is_ajax_request():
                return json_response(error_msg, 500)
            flash('An error occurred. Please try again.', 'error')
            return redirect(url_for('logInExistingUser'))

    return render_template('login.html')

@app.route('/')
def homePage():
    """Handle the home page."""
    if 'userId' in session:
        try:
            user = Users.query.get(session['userId'])
            if is_ajax_request():
                return json_response({'user': user.to_dict()})
            return render_template('home.html', user=user)
        except Exception as e:
            logger.error(f"Error loading home page: {str(e)}")
            session.clear()
            if is_ajax_request():
                return json_response({
                    'error': 'server_error',
                    'message': 'An error occurred loading the page'
                }, 500)
            flash('An error occurred. Please try again.', 'error')
            return redirect(url_for('logInExistingUser'))
    return render_template('index.html')

@app.route('/home')
@login_required
def loggedInHomePage():
    """Handle logged-in home page."""
    try:
        user = Users.query.get(session['userId'])
        if is_ajax_request():
            return json_response({'user': user.to_dict()})
        return render_template('home.html', user=user)
    except Exception as e:
        logger.error(f"Error loading logged-in home page: {str(e)}")
        if is_ajax_request():
            return json_response({
                'error': 'server_error',
                'message': 'An error occurred loading the page'
            }, 500)
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('logInExistingUser'))

@app.route('/logout')
def logout():
    """Handle user logout."""
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
    """Check email availability."""
    try:
        email = request.form.get('email')
        exists = Users.query.filter_by(email=email).first() is not None
        return json_response({'exists': exists})
    except Exception as e:
        logger.error(f"Error checking email: {str(e)}")
        return json_response({
            'error': 'server_error',
            'message': 'An error occurred checking the email'
        }, 500)

@app.route('/validate-password', methods=['POST'])
def validatePassword():
    """Validate password strength."""
    try:
        password = request.form.get('password')
        is_valid, validations = validate_password(password)
        return json_response({
            'valid': is_valid,
            'validations': validations
        })
    except Exception as e:
        logger.error(f"Error validating password: {str(e)}")
        return json_response({
            'error': 'server_error',
            'message': 'An error occurred validating the password'
        }, 500)

# Protected Quiz Routes
@app.route('/playquiz')
@login_required
def quizPage():
    """Quiz selection page."""
    try:
        user = Users.query.get(session['userId'])
        return render_template('choosequiz.html', user=user)
    except Exception as e:
        logger.error(f"Error loading quiz page: {str(e)}")
        if is_ajax_request():
            return json_response({
                'error': 'server_error',
                'message': 'An error occurred loading the quiz page'
            }, 500)
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('loggedInHomePage'))

@app.route('/random-quiz')
@login_required
def randomQuiz():
    """Random quiz page."""
    try:
        user = Users.query.get(session['userId'])
        return render_template('singlequiz.html', user=user)
    except Exception as e:
        logger.error(f"Error loading random quiz: {str(e)}")
        if is_ajax_request():
            return json_response({
                'error': 'server_error',
                'message': 'An error occurred loading the quiz'
            }, 500)
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('quizPage'))

@app.route('/profile')
@login_required
def userProfile():
    """User profile page."""
    try:
        user = Users.query.get(session['userId'])
        return render_template('comingsoon.html', user=user)
    except Exception as e:
        logger.error(f"Error loading profile: {str(e)}")
        if is_ajax_request():
            return json_response({
                'error': 'server_error',
                'message': 'An error occurred loading the profile'
            }, 500)
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('loggedInHomePage'))

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    if is_ajax_request():
        return json_response({
            'error': 'not_found',
            'message': 'Page not found'
        }, 404)
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(e)}")
    if is_ajax_request():
        return json_response({
            'error': 'server_error',
            'message': 'An internal server error occurred'
        }, 500)
    flash('An internal server error occurred', 'error')
    return redirect(url_for('logInExistingUser'))

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()  # Create database tables
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Error creating database tables: {str(e)}")
    
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
