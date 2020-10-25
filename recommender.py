import pandas as pd
import numpy as np


CHAMP = pd.read_csv("champions.csv")

CHAMP_NAMES = list(CHAMP["Champions"])
STAT_NAMES  = [
    "HP", "HP+", "HP5", "HP5+", "MP", "MP+", "MP5", "MP5+", "AD", "AD+", 
    "AS", "AS+", "AR", "AR+", "MR", "MR+", "MS", "Range"
]

CHAMP_STATS = CHAMP.drop(columns=["Champions", "Primary"])
CHAMP_ARRAY = (CHAMP_STATS-CHAMP_STATS.min())/(CHAMP_STATS.max()-CHAMP_STATS.min())
CHAMP_ARRAY= np.array(CHAMP_ARRAY)


def coseno(ele_a, ele_b):
    dot = np.dot(ele_a, ele_b)
    norma = np.linalg.norm(ele_a)
    normb = np.linalg.norm(ele_b)
    cos = dot / (norma * normb)
    return(float(cos))


def recoms(nombre, cuantos=14, matriz=CHAMP_ARRAY, nombres=CHAMP_NAMES):
    posicion = nombres.index(nombre)
    resultados = [coseno(i, matriz[posicion]) for i in matriz]
    resultados = [np.round(i*100, 2) for i in resultados]
    recs = list(tuple(zip(resultados, nombres)))
    recs = sorted(recs, reverse = True)
    return(recs[1:cuantos+1])


def get_stats(nombre, tabla=CHAMP, nombres=STAT_NAMES):
    renglon = tabla.loc[tabla["Champions"] == nombre, STAT_NAMES]
    valores = renglon.values.flatten().tolist()
    ajustados = []
    for i in valores:
        if i.is_integer():
            ajustados.append(int(i))
        else:
            ajustados.append(np.round(i, 3))
    stats = list(tuple(zip(nombres, ajustados)))
    return stats


def get_role(nombre, tabla=CHAMP):
    rol = tabla.loc[tabla["Champions"] == nombre, "Primary"]
    rol = str(rol.values[0])
    return rol
