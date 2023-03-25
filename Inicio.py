import streamlit as st

def main():
    """Exemplos de acesso ao api openai"""
    st.title("GPTreco")
    st.subheader("Para facilitar o teste e medição")
    st.warning("secrets.toml armazena suas credencias. Fique atento")

    #if st.button("Signup"):
    #    st.success("You have successfully created a valid Account")   

    #st.info("Go to Login Menu to login")
    st.write("Batepronto - perguntas e respostas")
    st.write("Chat - Conversa contínua")

if __name__ == '__main__':
	main()
