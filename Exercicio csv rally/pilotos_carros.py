"""Programa para ler e guardar dados em ficheiros csv para carros pilotos de corridas.
carros.csv : marca,modelo,matricula
pilotos.csv: nome,idade,pais

Funcionalidades
    adicionar: carros,pilotos
    Listar: carros, pilotos
    Pesquisar: pilotos de um carro, carro de um piloto
"""

import csv
import os

FICHEIRO_PILOTOS = "pilotos.csv"
FICHEIRO_CARROS = "carros.csv"

lista_pilotos = []
lista_carros = []

def LerFicheiro(nome_ficheiro):
    "Função para ler ficheiro csv e devolver uma lista com os dados"
    # lista vazia para guardar os dados do ficheiro
    dados = []
    # verificar se o ficheiro existe
    if os.path.exists(nome_ficheiro) == False:
        return dados
    # abrir o ficheiro para leitura
    with open(nome_ficheiro,"r",encoding="utf-8") as ficheiro:
        # criar o objeto para ler o csv
        ler = csv.DictReader(ficheiro)

        # ler cada linha do ficheiro e adicionar a lista
        for linha in ler:
            dados.append(linha)

    # devolver a lista com os dados do ficheiro:
    return dados

def Escrever(lista,nome):
    """Função para escrever os dados de uma lista num ficheiro csv"""
    # cabeçalho do ficheiro csv
    chaves = lista[0].keys()
    with open(nome,"w",encoding="utf-8",newline="") as ficheiro:
        # variavel para gravar no ficheiro (ficheiro,campos do dicionario)
        escrever = csv.DictWriter(ficheiro,fieldnames=chaves)
        # gravar o cabeçalho
        escrever.writeheader()
        for i in range(len(lista)):
            escrever.writerow(lista[i]) # grava os dados correspondentes as chaves           

def ValidarMatricula(matricula):
    """Devolve true se a matricula existe ou false se não existir"""
    for carro in lista_carros:
        if carro["matricula"] == matricula:
            return True
    return False

def Adicionar():
    op = input("Adicionar [P]iloto ou [C]arro? \n op:")
    if op in "cC":
        # ler os dados dos carros
        marca = input("insira a marca do carro: ")
        modelo = input("insira o modelo do carro: ")
        matricula = input("insira a matricula do carros (AA): ")
        if ValidarMatricula(matricula) == True:
            print("Matrícula já existe")
            return 
        # criar um dicionario
        carros = {"marca":marca,"modelo":modelo,"matricula":matricula}
        # adicionar a lista
        lista_carros.append(carros)
        # escrever no ficheiro dos carros
        Escrever(lista_carros,FICHEIRO_CARROS)

    if op in "pP":
        # ler os dados dos pilotos
        matricula = input("Introduza a matricula do veiculo: ")
        # verificar se a matricula do carro existe
        if ValidarMatricula(matricula) == False:
            print("Matrícula introduzida não existe. ")
            return
        nome = input("Introduza o nome do piloto: ")
        idade = int(input("Introduza a idade do piloto: "))
        pais = input("Introduza o país do piloto: ")
        # criar um dicionario
        piloto = {"nome":nome,"idade":idade,"pais":pais,"matricula":matricula}
        # adicionar a lista
        lista_pilotos.append(piloto)
        # escrever no ficheiro dos pilotos 
        Escrever(lista_pilotos,FICHEIRO_PILOTOS)
        print("O piloto foi adicionado com sucesso.")

def Listar():
    op = input("Adicionar [P]iloto ou [C]arro? \n op:")
    if op in "cC":
        print(lista_carros)
    if op in "pP":
        print(lista_pilotos)

def Pesquisar():
    pass

def Menu():
    global lista_pilotos , lista_carros
    lista_carros = LerFicheiro(FICHEIRO_CARROS)
    lista_pilotos = LerFicheiro(FICHEIRO_PILOTOS)
    op = 0
    while op != 4:
        op = int(input("1.Adicionar\n2.Listar\n3.Pequisar\n4.Sair\nop: "))
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Pesquisar()     

if __name__ == "__main__":
    Menu()