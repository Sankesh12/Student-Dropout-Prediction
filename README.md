# 🎓 Student Dropout Prediction

- A Machine Learning project that predicts whether a student is likely to drop out based on academic performance, student characteristics, family background, study habits, and other relevant factors.

- This project was developed as part of my **Big Brains Internship** to practice an end-to-end Machine Learning workflow, from data exploration and preprocessing to model training, evaluation, and application deployment.

---

## 📌 Project Overview

- Student dropout is an important educational problem. Identifying students who may be at risk can help educational institutions take early action and provide appropriate support.

- The goal of this project is to build a classification model that predicts the student's dropout outcome based on available student information.

The project includes:

* Exploratory Data Analysis
* Data cleaning
* Feature analysis
* Categorical feature encoding
* Numerical feature scaling
* Logistic Regression
* Model evaluation
* Model serialization
* Streamlit application
* Deployment

---

## 🎯 Problem Statement

- Build a Machine Learning classification system that can predict whether a student is likely to drop out based on academic, demographic, family, and behavioral features.

### Target Variable

`Dropped_Out`

* `0` → Not Dropout
* `1` → Dropout

---

## 📊 Dataset

The dataset contains:

* **649 student records**
* **34 columns**
* Numerical and categorical features

The features include information such as:

* School
* Gender
* Age
* Family size
* Parental status
* Mother and father education
* Mother and father occupation
* Study time
* Number of failures
* School support
* Family support
* Internet access
* Absences
* Grade 1
* Grade 2
* Final Grade

---

## 🔎 Exploratory Data Analysis

- EDA was performed to understand the structure and relationships within the dataset.

The analysis included:

* Dataset shape and structure
* Data types
* Statistical summaries
* Missing-value checking
* Duplicate checking
* Dropout distribution
* Academic-performance analysis
* Failure analysis
* Study-time analysis
* Absence analysis
* Feature relationships
* Correlation heatmap

### Important Findings

- The EDA showed that academic performance and previous failures have noticeable relationships with dropout outcomes.

Important numerical features included:

* `Final_Grade`
* `Grade_2`
* `Grade_1`
* `Number_of_Failures`
* `Study_Time`

Some categorical features such as school type and intention to pursue higher education also showed differences in dropout rates.

---

## ⚙️ Data Preprocessing

The following preprocessing steps were applied:

### 1. Separate Features and Target

`Dropped_Out` was separated from the input features.

### 2. Categorical Features

Categorical features were identified automatically using:

```python
X.select_dtypes(include=["object", "category"])
```

They were converted using:

```python
OneHotEncoder(handle_unknown="ignore")
```

### 3. Numerical Features

Numerical features were standardized using:

```python
StandardScaler()
```

### 4. Train-Test Split

The dataset was divided into:

* **80% training data**
* **20% testing data**

Stratified splitting was used to maintain the target-class distribution.

---

## 🤖 Machine Learning Model

### Logistic Regression

- Logistic Regression was selected as the classification model.

The complete workflow was implemented using a Scikit-learn Pipeline:

```text
Raw Data
    ↓
Categorical Encoding
    ↓
Numerical Scaling
    ↓
Logistic Regression
    ↓
Prediction
    ↓
Evaluation
```

Using a pipeline ensures that preprocessing and prediction remain together and can be reused when making predictions on new student data.

---

## 📈 Model Performance

The model was evaluated on the 20% test set.

| Metric            | Result |
| ----------------- | -----: |
| Accuracy          | 96.92% |
| ROC-AUC           | 97.86% |
| Dropout Precision | 90.00% |
| Dropout Recall    | 90.00% |
| Dropout F1-Score  | 90.00% |

### Confusion Matrix

```text
[[108   2]
 [  2  18]]
```

The model correctly classified most students in the test dataset, while making a small number of incorrect predictions.

---

## 🌐 Streamlit Application

A Streamlit web application was created to allow users to enter student information and receive a dropout prediction.

The application provides:

* Student information input
* Dropout probability
* Risk level
* Dropout / Not Dropout prediction

### Risk Levels

```text
Probability < 40%  → Low Risk
40%–69%            → Medium Risk
70%+               → High Risk
```

The application is intended as a demonstration of how a Machine Learning model can be integrated into a simple educational prediction tool.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-dropout-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
student-dropout-prediction/
│
├── app.py
├── student_dropout.csv
├── model.pkl
├── student_dropout_prediction.ipynb
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge&logo=numpy) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Joblib](https://img.shields.io/badge/Joblib-Model%20Serialization-success?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit)

---

## 📚 Learning Outcomes

Through this project, I practiced:

* Exploratory Data Analysis
* Data preprocessing
* Feature engineering concepts
* Categorical encoding
* Feature scaling
* Classification
* Logistic Regression
* Model evaluation
* ROC-AUC
* Confusion matrix
* Machine Learning pipelines
* Model serialization
* Streamlit development
* GitHub project documentation
* ML application deployment

---

## 📊 Results & Conclusion

- The Logistic Regression model achieved 96.92% accuracy and a 97.86% ROC-AUC score on the test data.

---

## 🚀 Future Work

- Try other Machine Learning models
- Add more student-related data
- Improve the Streamlit UI

---

## 👨‍💻 Author

**Sankesh Lal**

Data Scientist | Python | Machine Learning | NLP | Scikit-learn | Streamlit | Open to Opportunities

This project was completed as part of my **Big Brains Internship**.

---

# 📬 Connect With Me

If you found this project helpful, feel free to connect with me or provide your feedback.

<p align="left">

<a href="https://www.linkedin.com/in/sankeshlal/" target="_blank">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="https://github.com/Sankesh12" target="_blank">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="mailto:sankesh.lal12@gmail.com">
<img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
</a>

</p>

⭐ **If you found this project useful, consider giving it a star on GitHub. It motivates me to build and share more machine learning projects.**
