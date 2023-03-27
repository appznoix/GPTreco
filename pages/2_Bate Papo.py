import openai
#import toml
import streamlit as st
import modules.count_token as ct
import modules.api_secret as sec

# def count_token(string:str, encoding_name = "gpt-3.5-turbo"):
#     """Returna numero de tokens em uma string."""
#     encoding = tiktoken.encoding_for_model(encoding_name)
#     #    encoding = tiktoken.get_encoding(encoding_name)
#     num_tokens = len(encoding.encode(string))
#     return num_tokens
    
def show_messages(text):
    messages_str = [
        f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][1:]
    ]
    msg =str("\n".join(messages_str))
    count = ct.count_token(msg)
    tokens = "" if count == 0 else "\nTokens: " + str(count)
    text.text_area("Messages", value=msg + tokens, height=400)    
    #text.text_area("Messages", value=str("\n".join(messages_str))+"\n"+count_token(messages_str), height=400)
    #text.text_area("Messages", value=str("\n".join(messages_str)), height=400)

openai.api_key  = sec.get_me_secret()
'''
with open("secrets.toml", "r") as f:
    config = toml.load(f)

openai.api_key = config["OPENAI_KEY"]
'''

BASE_PROMPT = [{"role": "system", "content": "You are a helpful assistant."}]

if "messages" not in st.session_state:
    st.session_state["messages"] = BASE_PROMPT

st.header("Bate papo com GPT-3 CHATBOT")

text = st.empty()
show_messages(text)

prompt = st.text_input(
    "Do que você quer falar?", value="", placeholder="Entre com as informações aqui...",
)

if st.button("Enviar"):
    with st.spinner("Gerando respostas..."):
        st.session_state["messages"] += [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=st.session_state["messages"]
        )
        message_response = response["choices"][0]["message"]["content"]
        st.session_state["messages"] += [
            {"role": "system", "content": message_response}
        ]
        show_messages(text)

if st.button("Limpar"):
    st.session_state["messages"] = BASE_PROMPT
    show_messages(text)
