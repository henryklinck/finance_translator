import bs4
import json
import os
import requests

URL_BASE = "https://investopedia.com/terms-beginning-with-"
JSON_FILE = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/app/static/data/definitions.json"
WORD_BLACKLIST = {"NOW", "WILL"}

def main():
    first_page = 4769351
    first_letter = 'a'

    definitions = {}

    for i in range(26):
        print(f"Scraping: {chr(ord(first_letter) + i).upper()}")

        page = requests.get(f"{URL_BASE}{chr(ord(first_letter) + i)}-{first_page + i}")
        
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        container = soup.find(id="dictionary-top300-list__content_1-0")

        terms = container.find_all("a")

        for term in terms:
            if term.text[-1] == ')':
                idx = term.text.find('(')
                if term.text[:idx - 1].upper() not in WORD_BLACKLIST:
                    definitions[term.text[:idx - 1].upper()] = term["href"]
                if term.text[idx + 1:-1].upper() not in WORD_BLACKLIST:
                    definitions[term.text[idx + 1:-1].upper()] = term["href"]
            else:
                if term.text.upper() not in WORD_BLACKLIST:
                    definitions[term.text.upper()] = term["href"]

    with open(JSON_FILE, "w") as f:
        json.dump(definitions, f, indent=4)

if __name__ == "__main__":
    main()
