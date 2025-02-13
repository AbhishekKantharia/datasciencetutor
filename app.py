import streamlit as st
import google.generativeai as ai
import os

# Configure API key securely (replace with st.secrets in production)
API_KEY = os.getenv("GOOGLE_API_KEY")  # Set this in environment variables
if not API_KEY:
    st.error("API Key is missing. Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

ai.configure(api_key="AIzaSyAtlJDZ6nAr13lUfeUNx4R4v7hoZkoYY-Q")

# System prompt for the AI model
sys_prompt = """You are a helpful AI Tutor for Data Science. 
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible. 
Make sure to take examples while explaining a concept.
If a student asks any question outside the data science scope, 
politely decline and tell them to ask questions only from the data science domain.
Always include a helpful statement at the end saying that:
'In case your query is not resolved, feel free to click on this link: 
[innomatics.in](https://innomatics.in) to get in touch with our mentor in a 1:1 Zoom call.'"""

gemini_model = ai.GenerativeModel(model_name="gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI
st.title("Data Science/AI Tutor")

user_input = st.text_area(label="Enter your query/issue", placeholder="Explain the concept of for loops")

btn_click = st.button("Get Answer")

if btn_click and user_input.strip():  # Ensure the input is not empty
    with st.spinner("Generating response..."):
        response = gemini_model.generate_content(user_input)

        if hasattr(response, "text"):
            st.write(response.text)
        else:
            st.error("Error: Unexpected response format. Please try again.")