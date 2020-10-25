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
        cols = row.find_all("td")
        new_cols = []
        for elem in cols:
            if elem.text.strip():
                new_cols.append(elem.text.strip())
            else: 
                if elem.img:
                    new_cols.append("OP")
                else:
                    new_cols.append(" ")
        elements = [ele for ele in new_cols if ele]
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


def limpiar_nums(list_nums):
    nums_limpios = []
    for nums in list_nums:
        nums = str(nums)
        nums = sub(r"\+|\%", "", nums)
        nums_limpios.append(float(nums))
    return(nums_limpios)


### Obtener data
# Roles
role_url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
role_class = "wikitable sortable"
role_df = crear_df(role_url, role_class)

# Base stats
base_url = "https://leagueoflegends.fandom.com/wiki/List_of_champions/Base_statistics"
base_class = "sortable wikitable sticky-header"
base_df = crear_df(base_url, base_class)
base_stats = [
    "HP", "HP+", "HP5", "HP5+", "MP", "MP+", "MP5", "MP5+", "AD", "AD+", 
    "AS", "AS+", "AR", "AR+", "MR", "MR+", "MS", "Range"
]

# Stats de Riot
riot_url = "https://leagueoflegends.fandom.com/wiki/List_of_champions/Ratings"
riot_class = "sortable"
riot_df = crear_df(riot_url, riot_class)
riot_stats = ["Damage", "Toughness", "Control", "Mobility", "Utility", "Difficulty"]
riot_colnames = [
    "Champions", "Primary", "Secondary", "Damage", "Toughness", "Control", "Mobility", "Utility", "Style", "DamageType", "Difficulty"
]

# Lane preferida
lane_url = "https://leagueoflegends.fandom.com/wiki/List_of_champions/Position"
lane_class = "article-table sortable"
lane_df = crear_df(lane_url, lane_class)
lane_colnames = [
    "Champions", "Top", "Jungle", "Mid", "Bottom", "Support", "Unplayed"
]
lane_roles = ["Top", "Jungle", "Mid", "Bottom", "Support"]


### Procesar data
base_df = base_df[~base_df.Champions.isin(["Mega Gnar", "Kled & Skaarl"])]
base_df = base_df.reset_index(drop=True)
base_df[base_stats] = base_df[base_stats].transform(limpiar_nums , axis=0)

riot_df.columns = riot_colnames
riot_df = riot_df[~riot_df.Champions.isin(["Mega Gnar", "Kled & Skaarl"])]
riot_df = riot_df.reset_index(drop=True)
riot_dummies = pd.get_dummies(
    riot_df[["Primary", "DamageType"]], 
    prefix=["Rol", "DType"]
)

lane_df.columns = lane_colnames
lane_df = lane_df.drop("Unplayed", axis=1)
lane_df = lane_df.replace(["OP", " "], [1, 0])

role_dummies = pd.get_dummies(role_df["Primary"], prefix="Rol")

# Exportar
champions = pd.concat([
    riot_df[["Champions", "Primary"]],
    base_df[base_stats],
    riot_df[riot_stats],
    riot_dummies,
    lane_df[lane_roles]
    ], axis = 1)

champions.to_csv("champions.csv", index=False)
