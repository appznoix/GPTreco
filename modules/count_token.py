import tiktoken

def count_token(string:str, encoding_name = "gpt-3.5-turbo"):
    """
    Retorna número de tokens em uma string, respeitando o encoding
    """
    encoding = tiktoken.encoding_for_model(encoding_name)
    return len(encoding.encode(string))

if __name__ == "__main__":    
    print("não execute diretamente")
    