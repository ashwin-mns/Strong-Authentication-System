import random
import string
import os
from fastapi import FastAPI, Request, Form, Depends, HTTPException, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from auth import PasswordManager
import db

app = FastAPI()
# Add a random secret key for sessions
app.add_middleware(SessionMiddleware, secret_key=os.urandom(24).hex())

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

pm = PasswordManager()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Flash messages from session
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    logged_in = request.session.get("logged_in", False)
    username = request.session.get("username", None)
    active_tab = request.session.pop("active_tab", "login")
    active_view = request.session.pop("active_view", None)
    
    user_data = None
    if username:
        user_data = db.get_user(username)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "error": error,
        "success": success,
        "logged_in": logged_in,
        "username": username,
        "user_data": user_data,
        "active_tab": active_tab,
        "active_view": active_view
    })

@app.post("/register")
async def register(
    request: Request, 
    username: str = Form(...), 
    password: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    dob: str = Form(...),
    gender: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...)
):
    # 1. Check if user exists
    if db.get_user(username):
        request.session["error"] = "Username already exists"
        request.session["active_tab"] = "register"
        return RedirectResponse(url="/", status_code=303)
    
    # 2. Validate Strength
    strength = pm.validate_strength(password, username)
    if not strength["is_strong"]:
        request.session["error"] = f"Password too weak: {strength['warning'] or 'Choose a more complex password.'}"
        request.session["active_tab"] = "register"
        return RedirectResponse(url="/", status_code=303)
    
    # 3. Hash and Store
    hashed = pm.hash_password(password)
    db.create_user(username, hashed, first_name, last_name, dob, gender, phone, email)
    
    request.session["success"] = "Registration successful! You can now log in."
    request.session["active_tab"] = "login"
    return RedirectResponse(url="/", status_code=303)

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = db.get_user(username)
    if not user:
        request.session["error"] = "Invalid username or password"
        request.session["active_tab"] = "login"
        return RedirectResponse(url="/", status_code=303)
    
    if pm.verify_password(password, user["hashed_password"]):
        request.session["logged_in"] = True
        request.session["username"] = username
        full_name = f"{user.get('first_name', '')} {user.get('last_name', '')}".strip() or username
        request.session["success"] = f"Welcome back, {full_name}!"
        return RedirectResponse(url="/", status_code=303)
    else:
        request.session["error"] = "Invalid username or password"
        request.session["active_tab"] = "login"
        return RedirectResponse(url="/", status_code=303)

@app.get("/forgot-password", response_class=HTMLResponse)
async def forgot_password_page(request: Request):
    request.session["active_view"] = "forgot"
    return RedirectResponse(url="/", status_code=303)

@app.post("/forgot-password")
async def process_forgot_password(request: Request, identifier: str = Form(...)):
    username, user_data = db.get_user_by_email_or_phone(identifier)
    if not username:
        request.session["error"] = "Account not found with that email/phone."
        request.session["active_view"] = "forgot"
        return RedirectResponse(url="/", status_code=303)
    
    otp = "".join(random.choices(string.digits, k=6))
    db.store_otp(username, otp)
    
    request.session["success"] = f"A reset code has been sent. (SIMULATED OTP: {otp})"
    request.session["active_view"] = "verify_otp"
    request.session["recovery_username"] = username
    return RedirectResponse(url="/", status_code=303)

@app.post("/verify-otp")
async def process_verify_otp(request: Request, username: str = Form(...), otp: str = Form(...)):
    if db.verify_otp(username, otp):
        request.session["active_view"] = "reset_password"
        request.session["recovery_username"] = username
        return RedirectResponse(url="/", status_code=303)
    else:
        request.session["error"] = "Invalid or expired OTP."
        request.session["active_view"] = "verify_otp"
        request.session["recovery_username"] = username
        return RedirectResponse(url="/", status_code=303)

@app.post("/reset-password")
async def process_reset_password(
    request: Request, 
    username: str = Form(...), 
    password: str = Form(...), 
    confirm_password: str = Form(...)
):
    if password != confirm_password:
        request.session["error"] = "Passwords do not match."
        request.session["active_view"] = "reset_password"
        request.session["recovery_username"] = username
        return RedirectResponse(url="/", status_code=303)
    
    strength = pm.validate_strength(password, username)
    if not strength["is_strong"]:
        request.session["error"] = f"Password too weak: {strength['warning']}"
        request.session["active_view"] = "reset_password"
        request.session["recovery_username"] = username
        return RedirectResponse(url="/", status_code=303)

    hashed = pm.hash_password(password)
    db.update_password(username, hashed)
    
    request.session["success"] = "Password set successfully! Please log in."
    request.session["active_tab"] = "login"
    return RedirectResponse(url="/", status_code=303)

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
