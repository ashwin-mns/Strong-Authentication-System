import json
import os
import time

DB_FILE = "database.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def get_user(username):
    db = load_db()
    return db.get(username)

def get_user_by_email_or_phone(identifier):
    db = load_db()
    for user, data in db.items():
        if data.get("email") == identifier or data.get("phone") == identifier:
            return user, data
    return None, None

def create_user(username, hashed_password, first_name, last_name, dob, gender, phone, email):
    db = load_db()
    if username in db:
        return False
    db[username] = {
        "hashed_password": hashed_password,
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob,
        "gender": gender,
        "phone": phone,
        "email": email
    }
    save_db(db)
    return True

def update_password(username, hashed_password):
    db = load_db()
    if username in db:
        db[username]["hashed_password"] = hashed_password
        save_db(db)
        return True
    return False

def store_otp(username, otp):
    db = load_db()
    if username in db:
        # OTP expires in 5 minutes
        db[username]["otp"] = {
            "code": otp,
            "expiry": time.time() + 300
        }
        save_db(db)
        return True
    return False

def verify_otp(username, otp):
    db = load_db()
    if username in db and "otp" in db[username]:
        otp_data = db[username]["otp"]
        if otp_data["code"] == otp and time.time() < otp_data["expiry"]:
            # Clear OTP after successful verification
            del db[username]["otp"]
            save_db(db)
            return True
    return False
