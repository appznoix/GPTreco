import streamlit as st
import modules.api_secret as sec

def main():
    """Exemplos de acesso ao api openai"""
    st.title("GPTreco")
    st.subheader("Exemplos de acesso ao API do chatGPT com contagem de tokens")
    secret = sec.get_me_secret()
    if secret in ['','OPENAI_KEY']:    
        st.warning("Armazene suas credencias openai em secrets.toml. Fique atento")
    st.write("Bate Pronto - Pergunta e resposta")
    st.write("Bate Papo - Conversa contínua")

if __name__ == '__main__':
	main()
