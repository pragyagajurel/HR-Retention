import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("pages/HR Employee Retention.csv")

st.title("Employee Retention Data Visualizations")

# Plot target variable distribution
st.subheader("Distribution of Employee Retention (Target Variable)")
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x=df["left"], palette="pastel", ax=ax)
ax.set_title("Distribution of Employee Retention")
ax.set_xlabel("Left (0 = Stayed, 1 = Left)")
ax.set_ylabel("Count")
st.pyplot(fig)

# Plot categorical variable distributions
st.subheader("Distribution of Employees by Department and Salary Level")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(x=df["sales"], palette="pastel", ax=axes[0])
axes[0].set_title("Employees by Department")
axes[0].set_xlabel("Department")
axes[0].set_ylabel("Count")
axes[0].tick_params(axis='x', rotation=90)

sns.countplot(x=df["salary"], palette="pastel", ax=axes[1])
axes[1].set_title("Employees by Salary Level")
axes[1].set_xlabel("Salary Level")
axes[1].set_ylabel("Count")

st.pyplot(fig)

# Numerical feature analysis
st.subheader("Numerical Feature Distributions by Employee Status")
numerical_features = ["satisfaction_level", "last_evaluation", "number_project", "average_montly_hours", "time_spend_company"]
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
axes = axes.flatten()
for i, feature in enumerate(numerical_features):
    sns.histplot(data=df, x=feature, hue="left", kde=True, palette="pastel", ax=axes[i])
    axes[i].set_title(f"Distribution of {feature} by Employee Status")
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel("Count")
plt.tight_layout()
st.pyplot(fig)
