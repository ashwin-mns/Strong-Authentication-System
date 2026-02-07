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

- <img width="1919" height="868" alt="Screenshot 2026-02-07 183431" src="https://github.com/user-attachments/assets/b03f243d-eac0-41fd-a2b3-93e51ca6a15f" />

<img width="1892" height="865" alt="Screenshot 2026-02-07 183501" src="https://github.com/user-attachments/assets/de5b86d0-164a-4033-bb11-e40711ae5427" />

<img width="1919" height="866" alt="Screenshot 2026-02-07 183603" src="https://github.com/user-attachments/assets/e8a40b21-2f78-44a9-80d8-6e220f16fc51" />

<img width="1919" height="882" alt="Screenshot 2026-02-07 184125" src="https://github.com/user-attachments/assets/e6a45c3e-f2a5-448e-86a7-34a257df957d" />

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
