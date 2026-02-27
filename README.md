🛡️ AI-Driven Threat Detection System

A full-stack AI-based cybersecurity system that detects malicious digital content in real-time.

This project includes:

🌐 Web Application Dashboard

🤖 Machine Learning Backend

🧩 Chrome Browser Extension

It detects:

Phishing URLs

Malicious Email Content

Suspicious Images

Suspicious Videos

📌 Project Overview

The AI-Driven Threat Detection System analyzes digital content using machine learning models and classifies it as:

🟢 SAFE / AUTHENTIC

🔴 THREAT DETECTED

The system returns:

Threat label

Confidence score (%)

Explanation message

This helps users identify phishing attacks and malicious content instantly.

🚀 Features
🔎 1. URL Detection

Detects phishing or fake URLs

Used in both Web App and Chrome Extension

Returns confidence percentage

📧 2. Email Analysis

Analyzes email content or headers

Detects phishing patterns using NLP

🖼️ 3. Image Analysis

Detects suspicious or manipulated images

Uses AI classification

🎥 4. Video Analysis

Upload video for basic AI-based threat detection

🌐 5. Chrome Extension (Real-Time URL Protection)

When extension is ON

Double-click any URL on a webpage

AI instantly checks whether it is safe or fake

Displays result in popup

🏗️ How It Works
Step 1: User Input

User enters:

URL

Email content

Image file

Video file

OR double-clicks URL using extension.

Step 2: Frontend Sends Request

Frontend sends API request to Flask backend.

Step 3: Backend Processing

Flask backend:

Extracts features

Sends data to trained ML model

Gets prediction

Step 4: Response

Backend returns:

{
  "label": 0,
  "confidence": 87,
  "message": "Suspicious phishing pattern detected."
}
Step 5: UI Display

Frontend displays:

Threat badge

Animated confidence ring

Explanation

🧠 Machine Learning

The system uses:

URL feature extraction

NLP text processing

Probability-based classification

Confidence scoring

Models are integrated into Flask APIs.

💻 Tech Stack
🔹 Frontend

HTML5

CSS3 (Glassmorphism UI)

JavaScript

Canvas background animation

Dark / Light theme toggle

🔹 Backend

Python

Flask

REST APIs

CORS enabled

🔹 Machine Learning

Scikit-learn

TensorFlow / Keras (if used)

🔹 Browser Extension

Chrome Manifest V3

JavaScript

Fetch API

📂 Project Structure
AI-Threat-Detection/
│
├── app.py
├── model.py
├── python_url_detector/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
│
├── extension/
│   ├── manifest.json
│   ├── background.js
│   ├── content.js
│   ├── popup.html
│   └── popup.js
│
└── README.md
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/ai-threat-detection.git
cd ai-threat-detection
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Backend Server
python app.py

Server runs at:

http://127.0.0.1:8080
4️⃣ Open Web App

Open browser:

http://127.0.0.1:8080
🧩 Install Chrome Extension

Open Chrome

Go to:

chrome://extensions/

Enable Developer Mode

Click Load Unpacked

Select extension/ folder

Now extension is ready 🎉

Double-click any URL to test detection.

🎨 UI Highlights

Premium Glassmorphism design

Animated background particles

Dark / Light mode with blur zoom transition

Circular confidence score ring

Real-time result section

🔐 Why This Project Matters

This system helps:

Prevent phishing attacks

Increase cybersecurity awareness

Provide real-time AI protection

Demonstrate practical ML integration

Showcase full-stack + AI development skills

📈 Future Improvements

Deploy on cloud (AWS / Render)

Add user authentication database

Real-time phishing blacklist integration

Auto-block malicious URLs in extension

Advanced deepfake detection

👨‍💻 Author

Anurag Tanpure
Aspiring Software Engineer
Java | Python | AI | Cybersecurity
