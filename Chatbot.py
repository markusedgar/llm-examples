import streamlit as st
import requests

# Configuration for allowed file types
ALLOWED_EXTENSIONS = ['jpg', 'txt', 'png', 'gif', 'bmp']

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_to_api(text_prompt, files, action):
    # This is a placeholder for the API call
    # In a real application, you would replace this with actual API logic
    api_url = "https://api.example.com/submit"  # Replace with your actual API endpoint

    # Prepare the data to send
    data = {
        "text_prompt": text_prompt,
        "action": action
    }

    files_data = []
    for file in files:
        files_data.append(("files", file))

    # In a real scenario, you might use requests.post() to send data to the API
    # For now, we'll just print what would be sent
    st.write("Data that would be sent to the API:")
    st.json(data)
    st.write("Files that would be uploaded:")
    for file in files:
        st.write(file.name)

    # Simulated API response
    return {"status": "success", "message": "Data received successfully"}

def main():
    st.title("File Upload and Processing App")

    # Text prompt
    text_prompt = st.text_area("Enter your text prompt here:", height=150)

    # File upload with type filtering
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=ALLOWED_EXTENSIONS)

    # Display allowed file types
    st.write(f"Allowed file types: {', '.join(ALLOWED_EXTENSIONS)}")

    # Action selection
    action = st.selectbox(
        "Select an action to perform on the data:",
        ["Process", "Analyze", "Transform"]
    )

    # Submit button
    if st.button("Submit"):
        if uploaded_files:
            # Filter out any files that don't meet the criteria (extra precaution)
            valid_files = [file for file in uploaded_files if is_allowed_file(file.name)]

            if len(valid_files) != len(uploaded_files):
                st.warning(f"Some files were ignored due to unsupported file types. {len(valid_files)} out of {len(uploaded_files)} files will be processed.")

            # Call the API (placeholder function)
            response = send_to_api(text_prompt, valid_files, action)

            # Display the API response
            st.write("API Response:")
            st.json(response)
        else:
            st.warning("Please upload at least one file before submitting.")

if __name__ == "__main__":
    main()
