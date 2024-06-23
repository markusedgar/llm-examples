import streamlit as st
import os
import openai

# Everything is accessible via the st.secrets dict:
# st.write("A cool secret:", st.secrets["OpenAI"]["openai_api_key"])

def get_openai_response(prompt, model):
    openai.api_key = st.secrets["OpenAI"]["openai_api_key"]
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

st.title("OpenAI Prompt Generator")

prompt = st.text_area("Enter your prompt:", height=200)
model = st.selectbox("Select the model:", ["davinci", "curie", "babbage", "ada"])

if st.button("Generate Response"):
    if prompt and model:
        response = get_openai_response(prompt, model)
        st.write("Response from OpenAI:", response)
    else:
        st.write("Please enter a prompt and select a model.")
