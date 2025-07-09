# Phishing Website Detector 🔍

A machine learning-based web application to detect whether a website URL is **phishing** or **legitimate**.  
The model is trained on URL-based features using **Logistic Regression** in Jupyter Notebook and deployed with a simple web interface.



## 📂 Project Structure
![image](https://github.com/user-attachments/assets/d7dae5cb-6fdf-45d1-949f-f233bff459e9)



---

## 🚀 Features

✅ Predicts if a URL is:
- **High-risk (Phishing)**
- **Moderate-risk**
- **Safe**

✅ Displays a **confidence score bar**, representing the model's probability that the URL is phishing:
- Higher confidence → higher risk
- Helps users understand how certain the model is about its prediction.

---

## 📊 How It Works

- The Logistic Regression model is trained on 30 URL-based features.
- Backend assigns `risk_label` as follows:
  - If `prediction == 1` → **High-risk**
  - Else if `confidence[1] > 0.5` → **Moderate-risk**
  - Else → **Safe**

- The confidence score bar visually shows the model’s confidence that the URL is phishing.

---

## 🛠️ Installation

### Clone the repository
```bash
git clone https://github.com/MalaikaAltaf/phishing_detector.git
cd phishing_detector

## 🛠️ Setup & Installation

### 📦 Set up virtual environment (optional but recommended)
It is recommended to use a virtual environment to isolate your dependencies:

python -m venv env
![image](https://github.com/user-attachments/assets/3f4bce05-97a0-4cc1-b6a3-a304f5ef1428)




