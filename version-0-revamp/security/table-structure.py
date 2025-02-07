"""
This Flask module stores the user's details
to the remote database using ORM.
Like other files in this directory, the
code was generated using ChatGPT.
"""
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DeviceLog(Base):
    __tablename__ = "device_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Link to Users table
    ip_address = Column(String(45), nullable=False)  # IPv4 or IPv6
    browser = Column(String(50), nullable=False)
    browser_version = Column(String(20))
    os = Column(String(50), nullable=False)
    os_version = Column(String(20))
    device = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="device_logs")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(254), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    device_logs = relationship("DeviceLog", back_populates="user")
