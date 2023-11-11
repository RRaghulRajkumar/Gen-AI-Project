"""
for mac:
pip install virtualenv
python -m venv myenv
source venv/bin/activate

for windows:
pip install virtualenv
python -m venv myenv
myenv\Scripts\activate
"""

import streamlit as st
import openai
import webbrowser

#Set your openai API Key 
openai.api_key=st.secrets["openai_api"]
st.title("Generative AI")
st.image("https://imgs.search.brave.com/RQObx8L5ROZSrVY8_Tyam3hwHmEC2IjES0fe4DtAy0c/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5nYXJ0cy5jb20v/ZmlsZXMvMTIvS2hh/YnktTGFtZS1QTkct/SW1hZ2UucG5n",width=200)
#Input Text Box
with st.sidebar:
    linkedin_url="https://www.linkedin.com/in/rraghulrajkumar/"
    github_url="https://github.com/RRaghulRajkumar"
    st.image("https://proinfluent.b-cdn.net/wp-content/uploads/2019/05/Logo-LinkedIn-officiel.png",width=100)
    if st.button("LinkedIn"):
         # Open the LinkedIn URL in a web browser
        webbrowser.open_new_tab(linkedin_url)
    st.image("https://imgs.search.brave.com/_kHkOj0rQGazc6sqY0ZeglYK_a8fA6vv2plHMAelW3Y/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL2ltYWdlcy81/ODQ3Zjk4ZmNlZjEw/MTRjMGI1ZTQ4YzAu/cG5n",width=70)
    if st.button("Github"):
         # Open the LinkedIn URL in a web browser
        webbrowser.open_new_tab(github_url)    




prompt=st.text_input("Enter A Prompt:")    
def generate_text(prompt):
    response=openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=12
    )
    return response.choices[0].text
#Button to generate text

if st.button("Generate"):
    if prompt:
        generate_text=generate_text(prompt)
        st.write("Generated Text")
        st.write(generate_text)
    else:
        st.warning("Please Enter a prompt")    