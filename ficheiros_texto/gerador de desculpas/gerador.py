"""programa para gerar deculpas"""
import random
import os

FICHEIRO_INTRO = "intro.txt"
FICHEIRO_CULPADO = "culpado.txt"
FICHEIRO_DESCULPA = "desculpa.txt"

def LinhaAleatoria(ficheiro):
    """função que devolve uma linha aleatoria de um ficheiro texto"""
    if os.path.exists(ficheiro) == False:
        print(f"Falta o ficheiro {ficheiro}")
        return ""
    with open(ficheiro,"r",encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
    linha = random.choice(linhas)
    linha = linha.replace("\n","")
    return linha

print(LinhaAleatoria(FICHEIRO_INTRO)+" ",end="")
print(LinhaAleatoria(FICHEIRO_CULPADO)+" ",end="")
print(LinhaAleatoria(FICHEIRO_DESCULPA)+".",end="")
