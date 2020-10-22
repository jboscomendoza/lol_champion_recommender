import pandas as pd
import numpy as np


champ = pd.read_csv("champions.csv")
champ = champ[~champ.Champions.isin(["Mega Gnar", "Kled & Skaarl"])]

champ_names = list(champ["Champions"])
champ_stats = champ.drop(columns="Champions")
champ_stats = np.array(champ_stats)

stat_names = list(champ.columns[1:])

def coseno(ele_a, ele_b):
    dot = np.dot(ele_a, ele_b)
    norma = np.linalg.norm(ele_a)
    normb = np.linalg.norm(ele_b)
    cos = dot / (norma * normb)
    return(float(cos))


def recoms(nombre, cuantos=14, matriz=champ_stats, nombres=champ_names):
    posicion = champ_names.index(nombre)
    resultados = [coseno(i, champ_stats[posicion]) for i in matriz]
    resultados = [np.round(i*100, 2) for i in resultados]
    recs = list(tuple(zip(resultados, nombres)))
    recs = sorted(recs, reverse = True)
    return(recs[1:cuantos+1])

def get_stats(nombre, tabla=champ, nombres=stat_names):
    renglon = tabla.loc[tabla["Champions"] == nombre, tabla.columns[1:]]
    valores = renglon.values.flatten().tolist()
    valores = [int(i) for i in valores]
    stats = list(tuple(zip(stat_names, valores)))
    return stats
