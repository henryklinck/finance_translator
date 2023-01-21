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
    tokens = int(1.5 * tokenize(prompt))
    co = initialize_cohere()
    response = co.generate(
        model='command-xlarge-nightly',  
        prompt=prompt,  
        max_tokens=tokens,  
        temperature=0.6)
    
    return response.generations[0].text
