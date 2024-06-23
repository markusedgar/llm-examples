import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key-here'

# Sidebar for settings
st.sidebar.title("Settings")
model = st.sidebar.selectbox(
    "Select Generative AI Model",
    ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]
)

# Main form
st.title("Generative AI Prompt Form")
with st.form(key='genai_form'):
    prompt = st.text_area("Enter your prompt here:")
    submit_button = st.form_submit_button(label='Generate')

if submit_button:
    if prompt:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=150
        )
        st.write("Response from OpenAI:")
        st.write(response.choices[0].text.strip())
    else:
        st.warning("Please enter a prompt.")
