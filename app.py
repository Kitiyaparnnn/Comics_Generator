import os
import openai
import streamlit as st
# from api_key import *

# Set up OpenAI API key
openai.api_key = ""

# Define function to generate completion
def generate_completion(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=25,
        temperature=0
    )
    return response.choices[0].text.strip()

# Define Streamlit app
def main():
    # Set page title
    st.set_page_config(page_title="OpenAI GPT-3 Text Generation")
    
    # Add page title
    st.title("OpenAI GPT-3 Text Generation")
    
    # Add text input for prompt
    prompt = st.text_input("Enter a prompt:", "Say this is a test")
    
    # Generate completion on button click
    if st.button("Generate Completion"):
        completion = generate_completion(prompt)
        st.write("Completion:", completion)

# Run Streamlit app
if __name__ == "__main__":
    main()
