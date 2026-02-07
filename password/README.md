# SecureAuth: Ultra-Strong Password Authentication & User Management

A high-security, professional web application for password authentication and user profile management, built with Python, FastAPI, and industry-standard cryptography.

## 🛡️ Advanced Security Features

- **Argon2id Hashing**: Uses the Password Hashing Competition winner (Argon2id). It is memory-hard and prevents GPU/ASIC brute-force attacks.
- **HMAC Peppering**: Adds a secret server-side key (pepper) before hashing. This ensures "blind" protection even if the database is leaked.
- **Zxcvbn Entropy Validation**: Real-time password strength estimation based on crack-time, not just simple character counts.
- **Forgot Password & OTP**: A full recovery flow using cryptographically secure 6-digit One-Time Passwords (OTP) with expiry times.
- **Session Security**: Uses `SessionMiddleware` (Starlette/itsdangerous) for secure state handling.
- **PRG Pattern**: Implements the "Post/Redirect/Get" pattern to prevent "Confirm Form Resubmission" warnings on page refresh.

## 🌈 UI/UX Features

- **Glassmorphism Design**: A premium "frosted glass" theme with backdrop blurs, soft gradients, and animated floating blobs.
- **Expanded Profiles**: Capture and display First Name, Last Name, DOB, Gender, Phone, and Email.
- **Interactive Forms**: Password visibility toggle (eye icon) and real-time strength meter.
- **Responsive Layout**: Fully optimized for mobile and desktop browsers.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the project.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
1. Start the server:
   ```bash
   python app.py
   ```
2. Open: `http://localhost:8000`

## 📂 Project Structure

- `app.py`: FastAPI server with Session and Redirect logic.
- `auth.py`: Cryptography core (Argon2id, HMAC, zxcvbn).
- `db.py`: Persistent JSON database with OTP and Profile support.
- `templates/index.html`: Main UI template with dynamic state views.
- `static/style.css`: Glassmorphic design system.
- `database.json`: Local storage for user credentials and profiles.

---
*Created with ❤️ for secure, modern authentication.*
