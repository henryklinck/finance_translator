import bs4
import json
import os
import requests

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
COMPANIES_FILE = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/app/static/data/companies.json"
SYMBOLS_FILE = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/app/static/data/symbols.json"
WORD_BLACKLIST = {"THE", "INC.", "INCORPORATED", "CORP.", "CORP", "CORPORATION", "COMPANY", "LLC"}

def main():
    companies = {}
    symbols = {}

    page = requests.get(URL)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    container = soup.find("tbody")
    rows = container.find_all("tr")
    
    for row in rows:
        data = row.find_all("a")
        if (data[0].text != "Symbol"):
            company = data[1].text.upper()
            for word in WORD_BLACKLIST:
                company = company.replace(word, "")
            company = company.strip()
            companies[company] = data[0].text
            symbols[data[0].text] = data[0].text

    with open(COMPANIES_FILE, "w") as f:
        json.dump(companies, f, indent=4)
    
    with open(SYMBOLS_FILE, "w") as f:
        json.dump(symbols, f, indent=4)

if __name__ == "__main__":
    main()
