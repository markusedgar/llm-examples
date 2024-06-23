import streamlit as st
import os

# Everything is accessible via the st.secrets dict:
st.write("A cool secret:", st.secrets["OpenAI"]["openai_api_key"])
