import cohere
from cohere.classify import Example
import json
import os
import re

def initialize_cohere():
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/api_key.json") as f:
        key = json.load(f)["key"]

    return cohere.Client(key)

def tokenize(input):
    co = initialize_cohere()

    return len(co.tokenize(input).token_strings)

def generate(input):

    # Classify the prompt: "economic" or "stock-related".
    subject = classify_text(input) 

    # Based on subject of input, prompt co:here ,command, to explain the input in simplier terms
    # prompt = 'Explain what this ' + subject + ' message means to a 5 year-old: \"' + input + '\" \n'
    # prompt = 'Do the foll0wing for the text:\n1. Find all of the finance terms that are in the text and list them in a dictionary format with key=term: value=description \n2. Extract the different companies involved \n3. Simplify the information \nText:' + input + '\" \n'
    prompt = 'Shorten and simplify what this ' + subject + ' message means: \"' + input + '\" \n'

    # Output should be a max size of input.length * 1.3
    tokens = round(1.3 * int(tokenize(input)))
    co = initialize_cohere()
    response = co.generate(
        model='command-xlarge-nightly',  
        prompt=prompt,  
        max_tokens=tokens,  
        temperature=0.9)
    
    return "Classification: " + subject + " --- \n " + response.generations[0].text

def classify_text(input):
    # Output whether propmt relates to:
    # 1.) The Overall Economy/Market (economic)
    # 2.) A Specific Investment (stock-related)

    # Opening market JSON file
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/cohere_training/market_text.json", 'r', encoding="cp437") as mrk_openfile:
 
        # Reading from market json file
        json_market_exs = json.load(mrk_openfile)

    # Opening investment JSON file
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/cohere_training/investment_text.json", 'r', encoding="cp437") as inv_openfile:
 
        # Reading from investment json file
        json_invest_exs = json.load(inv_openfile)

    examples = [];

    for i in range(6):
        curr_example = Example(json_market_exs[str("example" + str(i + 1))], "economic")
        examples.append(curr_example)
        curr_example = Example(json_invest_exs[str("example" + str(i + 1))], "stock-related")
        examples.append(curr_example)

    co = initialize_cohere()

    response = co.classify(
        model='small',
        inputs=[input],
        examples=examples)
    
    # Returns prediction: "economic" or "stock-related"
    return response.classifications[0].prediction

