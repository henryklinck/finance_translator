import json
import os

COMPANIES_FILE = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/static/data/companies.json"
SYMBOLS_FILE = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/static/data/symbols.json"

class CompanyTrieNode:
    def __init__(self):
        self.company = None
        self.symbol = None
        self.children = {}

def add_to_company_trie(root, company, i, symbol):
    if i < len(company):
        char = company[i]
        if char not in root.children:
            root.children[char] = CompanyTrieNode()
        add_to_company_trie(root.children[char], company, i + 1, symbol)
    elif i == len(company):
        root.company = company
        root.symbol = symbol

def generate_company_trie():
    root = CompanyTrieNode()
    companies = {}

    with open(COMPANIES_FILE, 'r') as f:
        companies = json.load(f)
    
    for company, symbol in companies.items():
        add_to_company_trie(root, company, 0, symbol)
    
    return root

class SymbolTrieNode:
    def __init__(self):
        self.symbol = None
        self.children = {}

def add_to_symbol_trie(root, symbol, i):
    if i < len(symbol):
        char = symbol[i]
        if char not in root.children:
            root.children[char] = SymbolTrieNode()
        add_to_symbol_trie(root.children[char], symbol, i + 1)
    elif i == len(symbol):
        root.symbol = symbol

def generate_symbol_trie():
    root = SymbolTrieNode()
    symbols = {}

    with open(SYMBOLS_FILE, 'r') as f:
        symbols = json.load(f)
    
    for symbol, s in symbols.items():
        add_to_symbol_trie(root, symbol, 0)

    return root

def get_companies(text):
    root = generate_company_trie()
    i = 0
    j = 0
    output = []

    while i < len(text) and j < len(text):
        current = root
        while j < len(text) and text[j].upper() in current.children:
            current = current.children[text[j].upper()]
            j += 1
            if current.company != None and (j == len(text) or text[j] in (' ', '.', ',')):
                output.append(current.symbol)
                current = root
                i = j = j + 1
                break
        else:
            if i != j:
                while i < len(text) and text[i] != ' ':
                    i += 1
                j = i = i + 1
            else:
                j += 1
    
    return output

def get_symbols(text):
    root = generate_symbol_trie()
    i = 0
    j = 0
    output = []

    while i < len(text) and j < len(text):
        current = root
        while j < len(text) and text[j] in current.children:
            current = current.children[text[j]]
            j += 1
            if current.symbol != None and (j == len(text) or text[j] in (' ', '.', ',')):
                output.append(current.symbol)
                current = root
                i = j = j + 1
                break
        else:
            if i != j:
                while i < len(text) and text[i] != ' ':
                    i += 1
                j = i = i + 1
            else:
                j += 1

    return output

def get_stocks(text):
    stock_set = set()
    stocks1 = get_companies(text)
    for stock in stocks1:
        stock_set.add(stock)
    stocks2 = get_symbols(text)
    for stock in stocks2:
        stock_set.add(stock)

    return stock_set
