import toml
def _get_api_secret_toml():
    # verifica se tem api no secrets.toml
    with open("secrets.toml", "r") as f: 
        config = toml.load(f)

    return config["OPENAI_KEY"]
    
def get_me_secret():
    return _get_api_secret_toml()
