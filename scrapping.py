import requests
import pandas as pd
from bs4 import BeautifulSoup
from re import sub

import numpy as np

base_url = "https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics"
base_resp = requests.get(base_url)
base_soup = BeautifulSoup(base_resp.text, "lxml")

base_soup.find("table", attrs = {"class": "sortable wikitable sticky-header jquery-tablesorter"})
base_table = base_soup.find_all("table")
base_champ = base_table[0]
base_rows = base_champ.find_all('tr')
base_name = base_champ.find_all('th')

headers = [i.text for i in base_name]
data = []

for row in base_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    elements = [ele for ele in cols if ele]
    elements[1:] = [float(sub(r"\D", "", ele)) for ele in elements[1:]]
    if len(elements) > 0:
        data.append(elements)

champions = pd.DataFrame(data, columns = headers)
champions.to_csv("champions.csv", index=False)