import streamlit as st
import openai
import modules.count_token as ct
import modules.api_secret as sec

st.title("Bate Pronto")
st.header("Pergunta e Resposta")
st.write("Exemplo de consulta simples ao api Completion openai")

st.sidebar.header("Instruções")
st.sidebar.info(
    """Esta aplicação permite que você interaja com
       uma implementação simples do API OpenAI do modelo ChatGPT e veja quantos tokens são emitidos
       Insira uma **consulta** na **caixa de texto** e **pressione enter** para receber
       uma **resposta** do ChatGPT. Você também pode escolher o módulo abaixo
    """
    )

# Set the model engine 
list = ['text-davinci-002','text-davinci-003']
model_engine = st.sidebar.selectbox("Escolha o módulo que deseja usar", list)
openai.api_key  = sec.get_me_secret()
def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response    
    '''    
    # Create a selectbox to allow the user to choose an AI module
    if(openai.api_key == '' or openai.api_key== 'OPENAI_KEY'):
        return st.warning("Pegue o Openai API Key: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) e salve-o no arquivo /secrets.toml")
    
    user_query = st.text_input("Como posso ajudar?", "")
    if user_query == ":q" or user_query == "":
        return st.warning("Aguardando sua pergunta!")
        
    [valid,response] = ChatGPT(user_query)
    if valid:
        count = ct.count_token(response)
        return st.write(f"{user_query} {response} \nTokens: {count}")
    
    return st.warning(f"{response}")


def ChatGPT(user_query):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    try:
        completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )        
        response = completion.choices[0].text
        return [True, response]
    except Exception as e:
        return [False, e.args[0]]


if __name__ == "__main__":
    main()

