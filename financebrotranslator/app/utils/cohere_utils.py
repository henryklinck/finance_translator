import cohere
import json
import os

def initialize_cohere():
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/api_key.json") as f:
        key = json.load(f)["key"]

    return cohere.Client(key)

def tokenize(prompt):
    co = initialize_cohere()

    return len(co.tokenize(prompt).token_strings)

def generate(prompt):

    prompt = 'Explain what this economic news means to a 5 year-old: \"' + prompt + '\" \n'

    tokens = int(tokenize(prompt))
    co = initialize_cohere()
    response = co.generate(
        model='command-xlarge-nightly',  
        prompt=prompt,  
        max_tokens=100,  
        temperature=0.9)
    
    return response.generations[0].text
