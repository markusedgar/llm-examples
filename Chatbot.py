import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]
# Sidebar for settings
st.sidebar.title("Settings")
model = st.sidebar.selectbox(
    "Select Generative AI Model",
    ["gpt-3.5-turbo", "gpt-4"]
)

# Main form
st.title("Generative AI Prompt Form")
with st.form(key='genai_form'):
    prompt = st.text_area("Enter your prompt here:")
    submit_button = st.form_submit_button(label='Generate')

if submit_button:
    if prompt:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        st.write("Response from OpenAI:")
        st.write(response.choices[0].message['content'].strip())
    else:
        st.warning("Please enter a prompt.")
