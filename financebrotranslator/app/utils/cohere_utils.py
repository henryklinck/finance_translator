import cohere
import json
import os
import re

def initialize_cohere():
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/api_key.json") as f:
        key = json.load(f)["key"]

    return cohere.Client(key)

def tokenize(prompt):
    co = initialize_cohere()

    return len(co.tokenize(prompt).token_strings)

def generate(prompt):
    # Current generate output is not great, need to continue to tweak prompts to improve performace.

    prompt_subject = generate_subject(prompt)

    prompt = 'Explain what this ' + prompt_subject + 'message means to a 5 year-old: \"' + prompt + '\" \n'

    tokens = int(tokenize(prompt))
    co = initialize_cohere()
    response = co.generate(
        model='command-xlarge-nightly',  
        prompt=prompt,  
        max_tokens=tokens,  
        temperature=0.9)
    
    return "Subject Prompt: " + prompt_subject + response.generations[0].text

def generate_subject(prompt):
    prompt = "List the subject in school would study this message: " + prompt + "\n \n Subject:" 

    tokens = int(tokenize(prompt))
    co = initialize_cohere()
    response = co.generate(
        model='command-xlarge-nightly',  
        prompt=prompt,  
        max_tokens=20,  
        temperature=0.9)

    return response.generations[0].text
