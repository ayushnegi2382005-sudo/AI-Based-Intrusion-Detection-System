# AI-Based Intrusion Detection System (IDS)

## 🚀 Overview

The AI-Based Intrusion Detection System (IDS) is a cybersecurity project designed to monitor live network traffic, identify suspicious activities, and enhance network security using Machine Learning. The system captures network packets in real time, extracts relevant features, and classifies traffic as normal or potentially malicious. It provides a user-friendly web dashboard for monitoring threats and can automatically block suspicious IP addresses while sending instant alerts.

## ✨ Features

* 🔍 Real-time network traffic monitoring
* 🤖 Machine Learning-based anomaly detection
* 🌐 Live packet capture using PyShark and TShark
* 🚫 Automatic blocking of suspicious IP addresses
* 📢 Real-time alert notifications
* 📊 Interactive Flask-based web dashboard
* ⚡ Lightweight and easy to deploy

## 🛠️ Technology Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

### Network Monitoring

* PyShark
* Wireshark / TShark

### Frontend

* HTML
* CSS
* JavaScript

## 📂 Project Structure

```text
AI-Based-Intrusion-Detection-System/
│
├── app.py
├── detector.py
├── models/
│   ├── anomaly_model.pkl
│   └── scaler.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Based-Intrusion-Detection-System.git
cd AI-Based-Intrusion-Detection-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Click **Start Detection** to begin monitoring network traffic.

## 🔐 How It Works

1. Captures live network packets using PyShark.
2. Extracts important traffic features.
3. Processes features through a trained Machine Learning model.
4. Detects anomalous or suspicious traffic patterns.
5. Displays alerts on the dashboard.
6. Optionally blocks suspicious IP addresses and sends notifications.

## 📸 Screenshots

Add screenshots of:

* Dashboard Home Page
* Live Detection Screen
* Alert Notifications
* Blocked IP Logs

## 🎯 Future Enhancements

* Deep Learning-based threat detection
* Attack type classification
* SIEM integration
* Threat intelligence feeds
* Email and SMS notifications
* Advanced analytics dashboard

## 👨‍💻 Author

Ayush Negi

Computer Science Student | Machine Learning & Cybersecurity Enthusiast

## 📜 License

This project is developed for educational and research purposes.
