import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=st.secrets["OpenAI"]["openai_api_key"]
)


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

    response_content = response
    print(response_content)

    return 'fun stuff'

    # return response['choices'][0]['text'].strip()

st.title("OpenAI Prompt Generator")

prompt = st.text_area("Enter your prompt:", height=200)
model = st.selectbox("Select the model:", ["gpt-4", "gpt-3.5-turbo", "gpt-3.5"])

if st.button("Generate Response"):
    if prompt and model:
        response = get_openai_response(prompt, model)
        st.write("Response from OpenAI:", response)
    else:
        st.write("Please enter a prompt and select a model.")
