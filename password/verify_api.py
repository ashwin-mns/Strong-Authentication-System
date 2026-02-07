import urllib.request
import urllib.parse
import time
import os

BASE_URL = "http://localhost:8000"

def test_auth_flow():
    print("--- Starting Auth Flow Verification ---")
    
    # 1. Test Registration
    print("1. Registering user...")
    reg_data = urllib.parse.urlencode({
        "username": "testuser",
        "password": "StrongPassword123!"
    }).encode()
    
    try:
        req = urllib.request.Request(f"{BASE_URL}/register", data=reg_data, method="POST")
        with urllib.request.urlopen(req) as response:
            body = response.read().decode()
            if "Registration successful" in body:
                print("   Registration: SUCCESS")
            elif "Username already exists" in body:
                print("   Registration: SUCCESS (User already exists)")
            else:
                print(f"   Registration: FAILED (Status: {response.status})")
                return
    except Exception as e:
        print(f"   Registration: FAILED ({e})")
        return

    # 2. Test Login
    print("2. Logging in...")
    login_data = urllib.parse.urlencode({
        "username": "testuser",
        "password": "StrongPassword123!"
    }).encode()
    
    try:
        req = urllib.request.Request(f"{BASE_URL}/login", data=login_data, method="POST")
        with urllib.request.urlopen(req) as response:
            body = response.read().decode()
            if "Welcome back, testuser" in body:
                print("   Login: SUCCESS")
            else:
                print("   Login: FAILED")
                return
    except Exception as e:
        print(f"   Login: FAILED ({e})")
        return

    # 3. Test Persistence
    print("3. Checking Persistence...")
    if os.path.exists("database.json"):
        print("   Persistence: SUCCESS (database.json found)")
    else:
        print("   Persistence: FAILED (database.json not found)")

    print("--- Verification Complete ---")

if __name__ == "__main__":
    time.sleep(2)
    test_auth_flow()
