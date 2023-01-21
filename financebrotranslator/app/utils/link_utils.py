import json
import os

DEFINITIONS_FILE = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/static/data/definitions.json"

class TrieNode:
    def __init__(self):
        self.word = None
        self.link = None
        self.children = {}

def add_to_trie(root, word, i, link):
    if i < len(word):
        char = word[i]
        if char not in root.children:
            root.children[char] = TrieNode()
        add_to_trie(root.children[char], word, i + 1, link)
    elif i == len(word):
        root.word = word
        root.link = link

def generate_trie():
    root = TrieNode()
    definitions = {}

    with open(DEFINITIONS_FILE, 'r') as f:
        definitions = json.load(f)
    
    for word, link in definitions.items():
        add_to_trie(root, word, 0, link)
    
    return root

def add_definition_links(text):
    root = generate_trie()
    i = 0
    j = 0
    output = ""

    while i < len(text) and j < len(text):
        current = root
        while j < len(text) and text[j].upper() in current.children:
            current = current.children[text[j].upper()]
            j += 1
            if current.word != None and (j == len(text) or text[j] in (' ', '.', ',')):
                output += f"<a href=\"{current.link}\">{text[i:j]}</a>"
                if j != len(text):
                    output += text[j]
                current = root
                i = j = j + 1
                break
        else:
            if i != j:
                start = i
                while i < len(text) and text[i] != ' ':
                    i += 1
                j = i = i + 1
                output += text[start:j]
                j -= 1
        j += 1
    

    return output
