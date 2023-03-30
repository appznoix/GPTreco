import openai
import streamlit as st
import modules.count_token as ct
import modules.api_secret as sec
    
def show_messages(text):
    messages_str = [
        f"{_['role']}: {_['content']}" for _ in st.session_state["messages"][1:]
    ]
    msg =str("\n".join(messages_str))
    count = ct.count_token(msg)
    tokens = "" if count == 0 else str(count)
    text.text_area("Mensagens", value=msg, height=400)    
    if count > 0 :
        st.write("Tokens: ", tokens)

openai.api_key  = sec.get_me_secret()

BASE_PROMPT = [{"role": "system", "content": "You are a helpful assistant."}]

if "messages" not in st.session_state:
    st.session_state["messages"] = BASE_PROMPT

st.title("Bate Papo")
st.header("Conversa contínua com ChatGPT Turbo")
st.write("Exemplo de consulta ao api ChatCompletion da Openai")

st.sidebar.header("Instruções")
st.sidebar.info(
    """Esta aplicação permite que você interaja com
       uma implementação simples do API ChatCompletion da OpenAI. O mesmo do modelo ChatGPT. Veja quantos tokens são emitidos.
       Insira uma **consulta** na **caixa de texto** e **pressione enter** para receber
       uma **resposta** do ChatGPT.
    """
    )

text = st.empty()
show_messages(text)

prompt = st.text_input(
    "Do que você quer falar?", value="", placeholder="Entre com as informações aqui...",
)

if prompt:
    with st.spinner("Gerando respostas..."):
        st.session_state["messages"] += [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=st.session_state["messages"]
        )
        message_response = response["choices"][0]["message"]["content"]
        st.session_state["messages"] += [
            {
                "role": "system", 
                "content": message_response
            }
        ]
        show_messages(text)

if st.button("Limpar"):
    st.session_state["messages"] = BASE_PROMPT
    show_messages(text)
