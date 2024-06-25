import streamlit as st
import pandas as pd
import io

def main():
    st.title("File Upload and Processing App")

    # Text prompt
    text_prompt = st.text_area("Enter your text prompt here:", height=150)

    # File upload
    allowed_extensions = ['csv', 'txt', 'xlsx']
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=allowed_extensions)

    # Action selection
    action = st.selectbox(
        "Select an action to perform on the data:",
        ["View Data", "Analyze Data", "Transform Data"]
    )

    if uploaded_files and action:
        st.write(f"You've selected to {action.lower()} the uploaded files.")

        for file in uploaded_files:
            file_extension = file.name.split('.')[-1]

            if file_extension == 'csv':
                df = pd.read_csv(file)
            elif file_extension == 'xlsx':
                df = pd.read_excel(file)
            elif file_extension == 'txt':
                content = file.getvalue().decode('utf-8')
                st.text_area(f"Content of {file.name}", content, height=200)
                continue

            if action == "View Data":
                st.write(f"Preview of {file.name}:")
                st.write(df.head())
            elif action == "Analyze Data":
                st.write(f"Analysis of {file.name}:")
                st.write(df.describe())
            elif action == "Transform Data":
                st.write(f"Transformed {file.name} (showing first 5 rows with doubled numeric values):")
                numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
                df[numeric_columns] = df[numeric_columns] * 2
                st.write(df.head())

    if text_prompt:
        st.write("Your text prompt:")
        st.write(text_prompt)

if __name__ == "__main__":
    main()
