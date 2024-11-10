import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import streamlit as st

# Add file uploader
st.title("Big Mart Dataset Analysis")
st.subheader("Upload Your CSV File")

# Use Streamlit's file uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Clean column names (remove leading/trailing whitespaces)
    df.columns = df.columns.str.strip()

    # Check the column names to debug the issue
    st.write("Column Names:", df.columns)

    # Show basic information about the dataset
    st.subheader("Dataset Overview")
    st.write(df.info())
    st.write(df.head())

    # Show summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Check for missing values
    st.subheader("Missing Values")
    missing_values = df.isnull().sum()
    st.write(missing_values)

    # Handle missing values by filling missing numerical columns with mean and categorical with mode
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)

    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)

    # Convert categorical variables using one-hot encoding
    df = pd.get_dummies(df, drop_first=True)

    # Visualize distribution of numerical columns
    st.subheader("Numerical Feature Distribution")
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        ax.set_title(f'Distribution of {col}')
        st.pyplot(fig)

    # Visualize correlation between numerical features
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

else:
    st.write("Please upload a CSV file to begin the analysis.")
