"""programa para copiar os itens de um ficheiro e inverter as linhas"""

import os

NOME_FICHEIRO = "batatas.txt"

with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
    lista = ficheiro.readlines()

with open("copia.txt","w",encoding="utf-8") as ficheiro:
    for i in range(len(lista),0,-1):
        ficheiro.write(lista[i-1])