# 🧠 Thyroid Cancer Detection – Machine Learning Project

This is a Machine Learning project built as part of my Data Science journey. The model predicts whether a thyroid condition is **Benign** or **Malignant** based on various medical and lifestyle inputs.

This project demonstrates the **complete ML pipeline**:  
✅ Data preprocessing  
✅ Model building  
✅ Evaluation  
✅ Web app deployment using Flask

---

## 📌 Objectives

- Analyze and preprocess thyroid cancer data
- Train a Logistic Regression model
- Evaluate model performance
- Build a Flask web app for real-time predictions

---

## 🧠 Features Used for Prediction

| Feature        | Description                                      |
|----------------|--------------------------------------------------|
| `age`          | Age of the patient                               |
| `tsh`, `t3`, `t4` | Thyroid hormone levels                        |
| `nodulesize`   | Size of thyroid nodules (in cm)                  |
| `gender`       | Male or Female                                   |
| `fhistory`     | Family history of thyroid cancer (Yes/No)        |
| `rexposer`     | Past exposure to radiation (Yes/No)              |
| `iodind`       | Iodine deficiency (Yes/No)                       |
| `smoking`      | Whether the person smokes                        |
| `obesity`      | Whether the person is obese                      |
| `diabetes`     | Diabetes status                                  |
| `rlevel`       | Risk level: Low / Medium / High                  |

---

## 📒 Jupyter Notebook Highlights

The Jupyter Notebook (`Thyroid Cancer Prediction.ipynb`) contains:

- Data exploration and summary statistics
- Missing value handling
- Feature encoding
- Model training with Logistic Regression
- Model evaluation
- Model saving with `pickle`

---

## 🌐 Web App Overview

Built using **Flask**, the app provides a clean UI where users can input patient data and get a prediction result.

- `thyroid_model.py`: Main Flask application
- `home.html`: Form for data entry
- `prediction.html`: Displays prediction results

---

## 🖼 Screenshots

> Replace these with your own images.

### 🔘 Input Form  
![Form Screenshot](screenshots/form.png)

### 📊 Prediction Result  
![Result Screenshot](screenshots/result.png)

---

## 🏃‍♂️ How to Run This Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/thyroid-cancer-detection.git
   cd thyroid-cancer-detection
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python thyroid_model.py
Open in your browser:

cpp
Copy
Edit
http://127.0.0.1:5000/
🛠 Tools & Technologies Used
📚 Languages & Libraries
Python

Pandas, NumPy

scikit-learn

Flask

Pickle

💻 Development & Visualization
Jupyter Notebook

HTML/CSS (Frontend)

Google Fonts

🔍 Model
Logistic Regression (with preprocessing and encoding)

📦 Deployment Ready
Flask Web App

requirements.txt for environment setup

👤 Author
Name: Your Full Name

Email: your.email@example.com

LinkedIn: linkedin.com/in/your-profile

GitHub: github.com/your-username

