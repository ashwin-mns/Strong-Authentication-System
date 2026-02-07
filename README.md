# SecureAuth: Ultra-Strong Password Authentication

A high-security, modern web application for password authentication built with Python, FastAPI, and heavy-duty cryptography.

## 🛡️ Security Features

- **Argon2id Hashing**: Uses the winner of the Password Hashing Competition. It is memory-hard and highly resistant to GPU/ASIC brute-force attacks.
- **HMAC Peppering**: Adds a server-side secret (pepper) to every password before hashing. Even if the database is stolen, cracking is impossible without the pepper.
- **Zxcvbn Entropy Validation**: Real-time password strength estimation based on crack-time, not just simple character rules.
- **JSON Persistence**: Stores hashed credentials in a local `database.json` file, ensuring user accounts persist across restarts.
- **Safe State Handling**: Minimal exposure of sensitive data in memory.

## 🌈 UI/UX Features

- **Glassmorphism Design**: A premium "frosted glass" light theme with backdrop blurs and floating interactive background blobs.
- **Password Visibility Toggle**: Interactive "eye" icon to show or hide the password field.
- **Responsive Layout**: Designed to look great on all screen sizes.
- **Real-time Feedback**: Dynamic strength bar and suggestions as you type your password.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository or navigate to the project folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. Start the FastAPI server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

## 📂 Project Structure

- `app.py`: The Main FastAPI web server.
- `auth.py`: Core security logic (Argon2, Pepper, Zxcvbn).
- `db.py`: Database operations and persistence logic.
- `templates/`: HTML templates for the UI.
- `static/`: CSS and other static assets.
- `database.json`: Local storage for hashed user data.

## 🧪 Documentation & Verification

- **Task List**: [task.md](file:///C:/Users/ashwi/.gemini/antigravity/brain/343201f3-64b5-46b1-9f4c-a2b3194b3a84/task.md)
- **Implementation Plan**: [implementation_plan.md](file:///C:/Users/ashwi/.gemini/antigravity/brain/343201f3-64b5-46b1-9f4c-a2b3194b3a84/implementation_plan.md)
- **Technical Walkthrough**: [walkthrough.md](file:///C:/Users/ashwi/.gemini/antigravity/brain/343201f3-64b5-46b1-9f4c-a2b3194b3a84/walkthrough.md)

---
*Created with ❤️ for secure authentication.*
