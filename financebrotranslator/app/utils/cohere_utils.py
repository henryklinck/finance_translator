import cohere
from cohere.classify import Example
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

    classify_subject = classify_text(prompt)

    prompt = 'Explain what this ' + prompt_subject + 'message means to a 5 year-old: \"' + prompt + '\" \n'

    tokens = int(tokenize(prompt))
    co = initialize_cohere()
    response = co.generate(
        model='command-xlarge-nightly',  
        prompt=prompt,  
        max_tokens=tokens,  
        temperature=0.9)
    
    return "Classify: " + str(classify_subject) + " .   Subject Prompt: " + prompt_subject + response.generations[0].text

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
<<<<<<< HEAD

def classify_text(prompt):
    # Output whether propmt relates to:
    # 1.) The Overall Economy/Market (m)
    # 2.) A Specific Investment (i)

    # Opening market JSON file
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/cohere_training/market_text.json", 'r') as mrk_openfile:
 
        # Reading from market json file
        json_market_exs = json.load(mrk_openfile)

    # Opening investment JSON file
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/cohere_training/investment_text.json", 'r') as inv_openfile:
 
        # Reading from investment json file
        json_invest_exs = json.load(inv_openfile)

    examples = [];

    for i in range(6):
        curr_example = Example(json_market_exs[str("example" + str(i + 1))], "m")
        examples.append(curr_example)
        curr_example = Example(json_invest_exs[str("example" + str(i + 1))], "i")
        examples.append(curr_example)

    co = initialize_cohere()

    response = co.classify(
        model='large',
        inputs=[prompt],
        examples=examples)
    
    return response
=======
>>>>>>> 6c1de87e9957b6799f9b12e3e53a7434a19a16e4
