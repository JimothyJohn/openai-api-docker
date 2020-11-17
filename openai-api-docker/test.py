import openai, os, re
import streamlit as st

regex = re.compile('[^a-zA-Z ]') # Characters to remove from output

openai.api_key = os.environ.get('OPENAI_API_KEY') # API Key for queries

st.title("Let me finish that for you...") # Page header
prompt = st.text_input('Input your sentence here:') # User input

if prompt:
    response = openai.Completion.create(engine="ada", prompt=prompt, max_tokens=5) # get response from OpenAI
    output = regex.sub('', prompt + response.choices[0].text) # Format output
    st.write(output) # Write output
