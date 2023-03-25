import streamlit as st
import toml
import openai
import tiktoken

st.title("Bate Pronto")
st.header("Perguntas e Respostas")
# st.sidebar.header("Instructions")
# st.sidebar.info(
#     '''This is a web application that allows you to interact with 
#        the OpenAI API's implementation of the ChatGPT model.
#        Enter a **query** in the **text box** and **press enter** to receive 
#        a **response** from the ChatGPT. You can also choose the module below
#        '''
#     )
st.sidebar.header("Instruções")
st.sidebar.info(
    '''Esta aplicação web permite que você interaja com
       a implementação da API OpenAI do modelo ChatGPT e ver quantos tokens são emitidos
       Insira uma **consulta** na **caixa de texto** e **pressione enter** para receber
       uma **resposta** do ChatGPT. Você também pode escolher o módulo abaixo
       '''
    )

# Set the model engine 
list = ['text-davinci-002','text-davinci-003']
model_engine = st.sidebar.selectbox("Escolha o módulo que deseja usar", list)

# Set your OpenAI API key
with open("secrets.toml", "r") as f:
    config = toml.load(f)

openai.api_key = config["OPENAI_KEY"]

if 'key' not in st.session_state:
    st.session_state['key'] = openai.api_key

if openai.api_key == "OPENAI_KEY":
    openai.api_key = st.sidebar.text_input("API Key", st.session_state['key'] , type="password")



def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response    
    '''    
    # Create a selectbox to allow the user to choose an AI module
    # Get user input
    user_query = st.text_input("Como posso ajudar?", "")
    # user_query = st.text_input("Enter query here, to exit enter :q", "what is Python?")
    if user_query == ":q" or user_query == "":
        return st.warning("Aguardando sua pergunta!")
        
    [valid,response] = ChatGPT(user_query)
    if valid:
        count = count_token(response)
        return st.write(f"{user_query} {response} \nTokens: {count}")
    
    
    return st.warning(f"{response}")
        
    # if user_query != ":q" or user_query != "":
    #     # Pass the query to the ChatGPT function
    #     response = ChatGPT(user_query)
    #     return st.write(f"{user_query} {response}")

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
        #errnum = e.args[0]
        #print(f"Unexpected {e=}, {type(e)=}")
        return [False, e.args[0]]
        #return errnum

def count_token(string:str, encoding_name = "cl100k_base"):
    """
    Retorna número de tokens em uma string.
    """
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
    
if __name__ == "__main__":
    main()

