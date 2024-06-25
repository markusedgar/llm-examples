import streamlit as st
import os
from openai import OpenAI
import requests

API_URL = "https://wpx-flowise.onrender.com/api/v1/prediction/00172756-ba9d-432b-bd8d-936f0478d63f"

def get_flowise_response(prompt, model):
    response = requests.post(API_URL, json={
        "question": prompt,
    })
    # We are not yet using the model parameter
    return response.json()

client = OpenAI(
    # This is the default and can be omitted
    api_key=st.secrets["OpenAI"]["openai_api_key"]
)

# models = client.models.list()
# st.write("Available models: ", models)


# Everything is accessible via the st.secrets dict:
# st.write("A cool secret:", st.secrets["OpenAI"]["openai_api_key"])

def get_openai_response(prompt, model):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model=model,
        max_tokens=150
    )

    return response.choices[0].message.content

    # return response['choices'][0]['text'].strip()



st.title("OpenAI Prompt Generator")

prompt = st.text_area("Enter your prompt:", height=200)
model = st.selectbox("Select the model:", ["gpt-4o", "gpt-4", "gpt-3.5-turbo"])

if st.button("Generate Response"):
    if prompt and model:
        response = get_flowise_response(prompt, model)
        st.write("Response from OpenAI:", response)
    else:
        st.write("Please enter a prompt and select a model.")
