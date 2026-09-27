import streamlit as st
import pandas as pd
import joblib

# Load model
model_pipeline = joblib.load("model.pkl")

st.title("🎓 Student Dropout Prediction")

st.write("Enter student information to predict dropout risk.")

# Student Information

School = st.selectbox("School", ["GP", "MS"])

Gender = st.selectbox("Gender", ["M", "F"])

Age = st.number_input("Age", 15, 25, 17)

Address = st.selectbox("Address", ["U", "R"])

Family_Size = st.selectbox("Family Size", ["LE3", "GT3"])

Parental_Status = st.selectbox(
    "Parental Status",
    ["T", "A"]
)

Mother_Education = st.number_input(
    "Mother Education", 0, 4, 2
)

Father_Education = st.number_input(
    "Father Education", 0, 4, 2
)

Mother_Job = st.selectbox(
    "Mother Job",
    ["teacher", "health", "services", "at_home", "other"]
)

Father_Job = st.selectbox(
    "Father Job",
    ["teacher", "health", "services", "at_home", "other"]
)

Reason_for_Choosing_School = st.selectbox(
    "Reason for Choosing School",
    ["home", "reputation", "course", "other"]
)

Guardian = st.selectbox(
    "Guardian",
    ["mother", "father", "other"]
)

Travel_Time = st.number_input("Travel Time", 1, 4, 1)

Study_Time = st.number_input("Study Time", 1, 4, 2)

Number_of_Failures = st.number_input(
    "Number of Failures", 0, 4, 0
)

School_Support = st.selectbox(
    "School Support", ["yes", "no"]
)

Family_Support = st.selectbox(
    "Family Support", ["yes", "no"]
)

Extra_Paid_Class = st.selectbox(
    "Extra Paid Class", ["yes", "no"]
)

Extra_Curricular_Activities = st.selectbox(
    "Extra Curricular Activities", ["yes", "no"]
)

Attended_Nursery = st.selectbox(
    "Attended Nursery", ["yes", "no"]
)

Wants_Higher_Education = st.selectbox(
    "Wants Higher Education", ["yes", "no"]
)

Internet_Access = st.selectbox(
    "Internet Access", ["yes", "no"]
)

In_Relationship = st.selectbox(
    "In Relationship", ["yes", "no"]
)

Family_Relationship = st.number_input(
    "Family Relationship", 1, 5, 3
)

Free_Time = st.number_input(
    "Free Time", 1, 5, 3
)

Going_Out = st.number_input(
    "Going Out", 1, 5, 3
)

Weekend_Alcohol_Consumption = st.number_input(
    "Weekend Alcohol Consumption", 1, 5, 1
)

Weekday_Alcohol_Consumption = st.number_input(
    "Weekday Alcohol Consumption", 1, 5, 1
)

Health_Status = st.number_input(
    "Health Status", 1, 5, 3
)

Number_of_Absences = st.number_input(
    "Number of Absences", 0, 100, 5
)

Grade_1 = st.number_input(
    "Grade 1", 0, 20, 10
)

Grade_2 = st.number_input(
    "Grade 2", 0, 20, 10
)

Final_Grade = st.number_input(
    "Final Grade", 0, 20, 10
)

if st.button("Predict Dropout Risk"):

    input_data = pd.DataFrame({
        "School": [School],
        "Gender": [Gender],
        "Age": [Age],
        "Address": [Address],
        "Family_Size": [Family_Size],
        "Parental_Status": [Parental_Status],
        "Mother_Education": [Mother_Education],
        "Father_Education": [Father_Education],
        "Mother_Job": [Mother_Job],
        "Father_Job": [Father_Job],
        "Reason_for_Choosing_School": [Reason_for_Choosing_School],
        "Guardian": [Guardian],
        "Travel_Time": [Travel_Time],
        "Study_Time": [Study_Time],
        "Number_of_Failures": [Number_of_Failures],
        "School_Support": [School_Support],
        "Family_Support": [Family_Support],
        "Extra_Paid_Class": [Extra_Paid_Class],
        "Extra_Curricular_Activities": [Extra_Curricular_Activities],
        "Attended_Nursery": [Attended_Nursery],
        "Wants_Higher_Education": [Wants_Higher_Education],
        "Internet_Access": [Internet_Access],
        "In_Relationship": [In_Relationship],
        "Family_Relationship": [Family_Relationship],
        "Free_Time": [Free_Time],
        "Going_Out": [Going_Out],
        "Weekend_Alcohol_Consumption": [Weekend_Alcohol_Consumption],
        "Weekday_Alcohol_Consumption": [Weekday_Alcohol_Consumption],
        "Health_Status": [Health_Status],
        "Number_of_Absences": [Number_of_Absences],
        "Grade_1": [Grade_1],
        "Grade_2": [Grade_2],
        "Final_Grade": [Final_Grade]
    })

    # Prediction
    prediction = model_pipeline.predict(input_data)[0]

    # Probability
    probability = model_pipeline.predict_proba(input_data)[0][1]

    # Risk level
    if probability >= 0.70:
        risk = "High Risk"
    elif probability >= 0.40:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    st.subheader("Prediction Result")

    st.metric(
        "Dropout Probability",
        f"{probability:.2%}"
    )

    st.write(f"### Risk Level: {risk}")

    if prediction == 1:
        st.error("⚠️ Student predicted as Dropout")
    else:
        st.success("✅ Student predicted as Not Dropout")