"""
Programa para ler até ao final do ficheiro
"""
import os

NOME_FICHEIRO = "pessoas.txt"

if os.path.exists(NOME_FICHEIRO) == False:
    print("O ficheiro não existe")
else:
    with open("pessoas.txt","r",encoding="utf-8") as ficheiro: 
        lista = ficheiro.readlines() 

    for nome in lista:
        print(nome,end="")

    # ou

    with open("pessoas.txt","r",encoding="utf-8") as ficheiro: 
        while True:
            linha = ficheiro.readline()
            # verificar se encontrou o fim do ficheiro (EOF) = end of file
            if not linha:
                break
            print(linha,end="")
