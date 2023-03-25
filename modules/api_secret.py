import streamlit as st
import toml
def get_api_secret_toml():
    # verifica se tem api no secrets.toml
    with open("secrets.toml", "r") as f: 
        config = toml.load(f)

    return config["OPENAI_KEY"]
    
def set_api_secret_session(secret):
    if 'key' not in st.session_state:
        st.session_state['key'] = secret

def input_api_secret(secret):
    if(secret == "OPENAI_KEY" or secret == "")  :        
        return st.sidebar.text_input("API Key", get_api_secret_section() , type="password")
    
    #return st.sidebar.text_input('segredor:',secret)
    return secret
    
def get_me_secret():
    secret = input_api_secret(get_api_secret_toml())
    if 'key' not in st.session_state:
        st.session_state['key'] = secret
        
    
    
def get_api_secret_section():    
    if 'key' in st.session_state:
        return st.session_state['key']
    return ''
