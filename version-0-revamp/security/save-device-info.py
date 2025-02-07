"""
This Python Flask module
saves the information from
the phone to the database table.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Replace with your actual database URI
DATABASE_URL = "sqlite:///example.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def save_device_info(user_id, device_data):
    session = SessionLocal()
    new_log = DeviceLog(
        user_id=user_id,
        ip_address=device_data['ip_address'],
        browser=device_data['browser'],
        browser_version=device_data['browser_version'],
        os=device_data['os'],
        os_version=device_data['os_version'],
        device=device_data['device']
    )
    session.add(new_log)
    session.commit()
    session.close()
