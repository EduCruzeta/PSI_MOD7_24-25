"""
Este é um programa que grava um dicionario com o módulo pickle
"""
import pickle

# ler dados
nome = input("Nome: ")
idade = input("Idade: ")
email = input("email: ")

# criar dicionario
registo = {"nome":nome,"idade":idade,"email":email}

# guardar num ficheiro
with open("so_um.dat","ab") as ficheiro:
    # serialização
    pickle.dump(registo,ficheiro)

print("Dados adicionados")