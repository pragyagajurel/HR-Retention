import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("pages/HR Employee Retention.csv")

def main():
    st.set_page_config(page_title="Employee Retention Analysis App", layout="wide")
    df = load_data()
    
    # App Title
    st.title("Employee Retention Analysis App")
    
    # App Description
    st.markdown(
        """
        ## About the App
        This application provides insights into employee retention using data analytics and machine learning.
        It allows users to explore key factors affecting employee attrition and make predictions on whether an 
        employee is likely to leave or stay.
        
        **Features:**
        - **Data Visualization:** Explore retention trends using interactive charts.
        - **Prediction Model:** Uses a trained **Random Forest Classifier** to predict employee retention.
        - **Feature Analysis:** Understand the key factors influencing employee turnover.
        
        ---
        ## Dataset Summary
        The dataset used in this project is the **HR Employee Retention dataset**, which contains records of employees
        with various attributes that help in predicting whether an employee will stay or leave.
        
        **Dataset Overview:**
        - **Total Records:** {len(df)}
        - **Features:**
          - `satisfaction_level`: Employee satisfaction level (0 to 1)
          - `last_evaluation`: Employee last performance evaluation (0 to 1)
          - `number_project`: Number of projects assigned to the employee
          - `average_montly_hours`: Average monthly working hours
          - `time_spend_company`: Total years spent in the company
          - `Work_accident`: Whether the employee had a workplace accident (0 or 1)
          - `left`: Target variable (0 = Stayed, 1 = Left)
          - `promotion_last_5years`: Whether promoted in the last 5 years (0 or 1)
          - `sales`: Department of the employee
          - `salary`: Salary category (low, medium, high)
        
        ---
        ## How to Use the App
        1. Navigate using the sidebar to explore different sections.
        2. Check out the **Visualizations** tab for insights into employee retention trends.
        3. Use the **Predictions** tab to input employee details and predict retention.
        
        Let's dive into the data and uncover insights!
        """
        
    )
    
# Dataset Preview
    st.write("### Sample Data")
    df = load_data()
    st.dataframe(df.head())

if __name__ == "__main__":
    main()
