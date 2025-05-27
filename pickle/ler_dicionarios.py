"""
Programa vai ler um ficheiro pickle e mostrar todos os dados
"""
import pickle

lista = []

with open("so_um.dat","rb") as ficheiro:
    while True:
        try:
            dados = pickle.load(ficheiro)
            print(dados)
            lista.apend(dados)
        except EOFError:
            break