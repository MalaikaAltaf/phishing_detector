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
Here’s the **nicely formatted full `.md` content** for just the **Setup & Run sections** with the parts you highlighted — ready to copy into your README or keep separate:

---

````markdown
## 🛠️ Setup & Installation

### 📦 Set up virtual environment (optional but recommended)
It is recommended to use a virtual environment to isolate your dependencies.

Create a virtual environment:
```bash
python -m venv env
````

---

### 🖥️ Activate the virtual environment

* On **Linux/Mac**:

  ```bash
  source env/bin/activate
  ```

* On **Windows**:

  ```bash
  env\Scripts\activate
  ```

---

## 📥 Install dependencies

Install all required Python packages using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the app

Start the Flask server:

```bash
python app.py
```

Then open your browser and navigate to:
🌐 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Model Training

The model was trained in **Jupyter Notebook** using:

* 📈 Logistic Regression
* 📝 30 URL-based features

The trained model is saved as:

```
phishing_model.pkl
```

---

## 📄 Requirements

All dependencies are listed in `requirements.txt`.
The main libraries used in this project are:

* Flask
* scikit-learn
* pandas
* numpy

---

## 🌟 Screenshot / Demo

![image](https://github.com/user-attachments/assets/bca53330-1e17-41ac-902d-bc3ec3282fae)








