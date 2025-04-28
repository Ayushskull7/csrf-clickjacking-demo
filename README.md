# 🛡️ CSRF and Clickjacking Demo on LinkedIn Clone (Educational Only)

This project is a **Flask** web application that **clones a LinkedIn login page** to **demonstrate CSRF (Cross-Site Request Forgery)** and **Clickjacking** attacks.

It is strictly for **educational and ethical hacking learning purposes** — helping you understand how common web vulnerabilities work and how to defend against them.

---

## 📂 Project Structure

```
.
├── templates/
│   ├── attacker_clickjacking.html    # Fake LinkedIn page used for Clickjacking attack
│   ├── home.html                    # Home page shown after login
│   ├── index.html                   # LinkedIn-style login page
│   ├── reset.html                   # Password reset page
├── login/                           # LinkedIn Login Page Assets
│   ├── sc/                          # Styles, scripts, and components for login page
│   │   ├── h/                       # Necessary files for LinkedIn login (styles, JS)
├── .gitignore                       # Ignore files (e.g., venv, .pyc, demo.db)
├── app.py                           # Main Flask application
├── demo.db                          # SQLite database (after initialization)
├── init_db.py                       # Script to initialize the database and add a demo user
├── requirements.txt                 # Python dependencies

```

---

## 🚀 Features

- **LinkedIn-styled Login page clone** (`index.html`)
- **User Login/Logout** functionality
- **Password Reset** with no CSRF protection (intentional for demo)
- **Session Management** using Flask `session`
- **Malicious CSRF Attack Simulation** (`/attacker`)
- **Clickjacking Attack Simulation** using iframe (`/clickjack`)
- **SQLite3 Database** to manage users

---

## ⚡ Attack Demonstrations

- **CSRF Attack:**
  - Visit [http://127.0.0.1:5000/attacker](http://127.0.0.1:5000/attacker)
  - This page silently submits a POST request to `/reset` changing your password without your permission.

- **Clickjacking Attack:**
  - Visit [http://127.0.0.1:5000/clickjack](http://127.0.0.1:5000/clickjack)
  - The page overlays a fake transparent button on an invisible iframe of the LinkedIn login page.
  - Victims are tricked into clicking buttons they don't see.

---

## 🛠️ How to Set Up and Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ayushskull7/csrf-clickjacking-demo.git
   cd csrf-clickjacking-demo
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate        # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the app**:
   ```bash
   python app.py
   ```

6. Open your browser and visit:
   ```
   http://127.0.0.1:5000/login
   ```

---

## 🔑 Default Login Credentials

| Username        | Password   |
|-----------------|------------|
| demo@gmail.com  | demo123    |

> These credentials are automatically created when you run `init_db.py`.

---

## 🔓 Hacked Credentials (For CSRF Demo)

As part of the **CSRF demonstration**, you can test the malicious attack using the following **hacked credentials**:

| Username        | Password   |
|-----------------|------------|
| demo@gmail.com  | hacked123  |

> **Important**: The password for `demo@gmail.com` will be **automatically updated** to `hacked123` when the CSRF attack is triggered by visiting [http://127.0.0.1:5000/attacker](http://127.0.0.1:5000/attacker).

---

## 🧩 Provided Files Summary

- `init_db.py`  
  Initializes the SQLite database with a sample user (`demo@gmail.com`).

- `templates/attacker_clickjacking.html`  
  A fake LinkedIn login page that hides a malicious clickjacking button.

- `templates/index.html`  
  The LinkedIn-styled **Login page**.

- `templates/home.html`  
  The **Home page** after login.

- `templates/reset.html`  
  The **Reset Password** page.

- `app.py`  
  Core server-side logic — manages login, session, reset, attacker pages, etc.

- `demo.db`  
  The SQLite database (auto-created after running `init_db.py`).

- `requirements.txt`  
  List of necessary Python packages.

---

## ⚠️ Disclaimer

> **This project is for educational purposes only.**
>  
> Do not use these vulnerabilities or this project for unauthorized or malicious attacks.

---

## ✨ What You Learn

- How real-world CSRF attacks work
- How real-world Clickjacking tricks users
- Why CSRF tokens, SameSite cookies, and security headers are important
- Why sensitive actions must require user re-authentication

