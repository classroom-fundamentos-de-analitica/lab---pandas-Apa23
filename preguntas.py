"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd
import numpy as np

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return tbl0.shape[0]


def pregunta_02():
    return tbl0.shape[1]


def pregunta_03():
    return tbl0["_c1"].value_counts().sort_index()


def pregunta_04():
    return tbl0.groupby("_c1").mean()["_c2"]


def pregunta_05():
    return tbl0.groupby("_c1").max()["_c2"]


def pregunta_06():
    return sorted(tbl1["_c4"].str.upper().unique())


def pregunta_07():
    return tbl0.groupby("_c1").sum()["_c2"]


def pregunta_08():
    tbl01 = tbl0.copy()
    tbl01['suma'] = tbl01.sum(axis=1)
    return tbl01.reset_index(drop=True)


def pregunta_09():
    tbl02 = tbl0.copy()
    tbl02["year"]=tbl02["_c3"].str.split("-", expand=True)[0]
    return tbl02


def pregunta_10():
    valores = tbl0[['_c1', '_c2']].groupby(['_c1'])['_c2'].apply(list).tolist()
    c2 = []

    for letra in valores:
        texto = ''
        for valor in sorted(letra):
            texto += f'{valor}:'
        
        c2.append(texto[:-1])

    return pd.DataFrame({
        '_c2': c2
    }, index = pd.Series(['A', 'B', 'C', 'D', 'E'], name='_c1'))

def pregunta_11():
    tbl04 = tbl1.copy()
    tbl04['_c4'] = tbl04.groupby(['_c0'])['_c4'].transform(lambda x : ''.join(x))
    tbl04 = tbl04.drop_duplicates()
    tbl04["_c4"] = tbl04["_c4"].apply(sorted)
    tbl04["_c4"] = tbl04["_c4"].apply(lambda x : ','.join(x))
    return tbl04.reset_index()[["_c0", "_c4"]]


def pregunta_12():
    tbl04 = tbl2.copy()
    tbl04["_c5b"]=tbl04["_c5b"].apply(str)
    tbl04=tbl04.sort_values(by=['_c5a', '_c5b'])
    tbl04['_c5'] = tbl04[['_c5a', '_c5b']].agg(':'.join, axis=1)
    tbl04['_c5'] = tbl04.groupby(['_c0'])['_c5'].transform(lambda x : ','.join(x))
    tbl04 = tbl04[["_c0","_c5"]].drop_duplicates()
    tbl04 = tbl04.sort_values("_c0")
    return tbl04.reset_index()[["_c0", "_c5"]]


def pregunta_13():
   summary = pd.merge(tbl0[["_c0", "_c1"]],tbl2[["_c0", "_c5b"]],on="_c0")
   return summary.groupby("_c1").sum()["_c5b"]
    
