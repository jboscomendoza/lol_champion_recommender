import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from re import sub


def crear_sopa(url):
    resp = requests.get(url)
    sopa = BeautifulSoup(resp.text, "lxml")
    return(sopa)


def crear_tabla(rows):
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        elements = [ele for ele in cols]
        #elements[1:] = [sub(r"\D", "", ele) for ele in elements[1:]]
        if len(elements) > 0:
            data.append(elements)
    return(data)


def crear_df(url, table_class):
    soup = crear_sopa(url)
    tble = soup.find("table", {"class": table_class})
    rows = tble.find_all("tr")
    name = tble.find_all("th")
    head = [i.text.strip() for i in name]
    data = crear_tabla(rows)
    df = pd.DataFrame(data, columns = head)
    return(df)


role_url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
role_class = "wikitable sortable"
role_df = crear_df(role_url, role_class)

base_url = "https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics"
base_class = "sortable wikitable sticky-header"
base_df = crear_df(base_url, base_class)
