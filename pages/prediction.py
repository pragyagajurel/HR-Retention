import streamlit as st
import pandas as pd
import joblib
import numpy as np
import sklearn
print(sklearn.__version__)
from sklearn.ensemble import RandomForestClassifier


# Load the trained model and scaler
model = joblib.load("best_model.pkl")
scaler = joblib.load("scalar.pkl")


# Streamlit UI
st.title("Employee Retention Prediction App")
st.write("Enter employee details to predict if they will stay or leave.")

# User input fields
satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
last_evaluation = st.slider("Last Evaluation Score", 0.0, 1.0, 0.5)
number_project = st.number_input("Number of Projects", 1, 10, 3)
average_montly_hours = st.number_input("Average Monthly Hours", 50, 400, 160)
time_spend_company = st.number_input("Years at Company", 1, 10, 3)
work_accident = st.selectbox("Had Work Accident?", [0, 1])
promotion_last_5years = st.selectbox("Got Promotion in Last 5 Years?", [0, 1])
salary = st.selectbox("Salary Level", ['low', 'medium', 'high'])
department = st.selectbox("Department", [
    'sales', 'accounting', 'hr', 'technical', 'support', 'management',
    'IT', 'product_mng', 'marketing', 'RandD'
])

# Encode salary
salary_mapping = {'low': 1, 'medium': 2, 'high': 3}
salary_encoded = salary_mapping[salary]

# One-hot encoding for department
department_encoded = [0] * 9  # 9 department options (excluding 'sales' as reference category)
department_list = ['RandD', 'accounting', 'hr', 'management', 'marketing', 'product_mng', 'support', 'technical', 'sales']
if department in department_list:
    index = department_list.index(department)
    department_encoded[index] = 1

# Prepare input data
input_data = np.array([
    satisfaction_level, last_evaluation, number_project, average_montly_hours,
    time_spend_company, work_accident, promotion_last_5years, salary_encoded
] + department_encoded).reshape(1, -1)

# Scale numerical features
input_data[:, :5] = scaler.transform(input_data[:, :5])

# Predict
if st.button("Predict Employee Retention"):
    prediction = model.predict(input_data)[0]
    result = "This employee is likely to STAY." if prediction == 0 else "This employee is likely to LEAVE."
    st.subheader(result)
