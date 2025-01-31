# This Python Script helps us to create
# a database table in MySQL using SQLAlchemy
#
# Helping with the import and use of
# environmental variables in this directory
import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from datetime import datetime


# Load the environmental variables from my .env file
load_dotenv()

# Storing the database URL from the .env file
myDbURL = os.getenv('SQLALCHEMY_DATABASE_URI')

Base = declarative_base()  # An instance of the declarative_base class


class User(Base):
    """
    A class that creates a User table in the remote database.

    Attributes:
        userId: The user's unique ID.
        firstname: User's first name.
        lastname: User's last name.
        email: User's email address.
        password: User's password (hashed).
        created_at: Timestamp when the user is created.
        updated_at: Timestamp when the user updates their profile.
        last_login: Timestamp of the last login session.
    """
    __tablename__ = 'users'  # The table name in the remote database
    userId = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    last_login = Column(DateTime, nullable=True)  # Updates at login

# Using a 'try - except' block to
# attempt the connection to the database
# try:
#     engine = create_engine(myDbURL, echo=True)
#     Base.metadata.create_all(engine)
#     print("✅ Connection Successful And Table Created Successfully!")
# except Exception as e:
#     print(f"❌ Connection failed, and table not created: {e}")
try:
    engine = create_engine(myDbURL, echo=True)
    Base.metadata.create_all(engine)
    print("Connection Successful And Table Created Successfully!")
except Exception as e:
    print(f"Connection failed, and table not created: {e}")
