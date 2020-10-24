import pandas as pd
import numpy as np


champ = pd.read_csv("champions.csv")

champ_names = list(champ["Champions"])
stat_names  = list(champ.columns[2:20])

champ_stats = champ.drop(columns=["Champions", "Primary"])
champ_stats = np.array(champ_stats)


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
    renglon = tabla.loc[tabla["Champions"] == nombre, stat_names]
    valores = renglon.values.flatten().tolist()
    ajustados = []
    for i in valores:
        if i.is_integer():
            ajustados.append(int(i))
        else:
            ajustados.append(np.round(i, 3))
    stats = list(tuple(zip(stat_names, ajustados)))
    return stats


def get_role(nombre, tabla=champ):
    rol = tabla.loc[tabla["Champions"] == nombre, "Primary"]
    rol = str(rol.values[0])
    return rol
