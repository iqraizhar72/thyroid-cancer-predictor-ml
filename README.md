# 🧠 Thyroid Cancer Detection – Machine Learning Project

This is a Machine Learning project built as part of my Data Science journey. The model predicts whether a thyroid condition is **Benign** or **Malignant** based on various medical and lifestyle inputs.

This project demonstrates the complete ML pipeline:

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

| Feature     | Description |
|-------------|-------------|
| `age`       | Age of the patient |
| `tsh`, `t3`, `t4` | Thyroid hormone levels |
| `nodulesize` | Size of thyroid nodules (in cm) |
| `gender`    | Male or Female |
| `fhistory`  | Family history of thyroid cancer (Yes/No) |
| `rexposer`  | Past exposure to radiation (Yes/No) |
| `iodind`    | Iodine deficiency (Yes/No) |
| `smoking`   | Whether the person smokes |
| `obesity`   | Whether the person is obese |
| `diabetes`  | Diabetes status |
| `rlevel`    | Risk level: Low / Medium / High |

---

## 📒 Jupyter Notebook Highlights

The Jupyter Notebook (`Thyroid Cancer Prediction.ipynb`) contains:

- ✅ Data exploration and summary statistics  
- ✅ Missing value handling  
- ✅ Feature encoding  
- ✅ Model training with Logistic Regression  
- ✅ Model evaluation  
- ✅ Model saving with pickle  

---

## 🌐 Web App Overview

Built using Flask, the app provides a clean UI where users can input patient data and get a prediction result.

- `thyroid_model.py` – Main Flask application  
- `templates/home.html` – Form for data entry  
- `templates/prediction.html` – Displays prediction results  

---

## 🖼 Screenshots

Replace these image paths with your actual screenshots (in a `/screenshots` folder):

### 🔘 Input Form
![Input Form](screenshots/form.png)

### 📊 Prediction Result
![Prediction Result](screenshots/result.png)

---

## 🏃‍♂️ How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/thyroid-cancer-detection.git
cd thyroid-cancer-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask App

```bash
python thyroid_model.py
```

### 4. Open in Your Browser

```cpp
http://127.0.0.1:5000/
```

## 🛠 Tools & Technologies Used

### 📚 Languages & Libraries
_Python

_Pandas, NumPy

_scikit-learn

_Flask

_Pickle

### 💻 Development & Visualization
_Jupyter Notebook

_HTML/CSS (Frontend)

_Google Fonts

### 🔍 Model
_Logistic Regression (with preprocessing and encoding)

### 📦 Deployment Ready
_Flask Web App

_requirements.txt for environment setup

## 👤 Author

**IqraIzhar**
- **LinkedIn:** [linkedin.com/in/iqra-izhar-08b8b8330](https://www.linkedin.com/in/iqra-izhar-08b8b8330)  
- **GitHub:** [github.com/iqraizhar72](https://github.com/iqraizhar72)
- **Email:** [iqraizhar72@gmail.com](mailto:iqraizhar72@gmail.com)
