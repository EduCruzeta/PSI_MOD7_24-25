"""desafio 08-05-2025"""

import os
from datetime import datetime

NOME_FICHEIRO = "Tarefas.txt"

def FicheiroExiste():
    if os.path.exists(NOME_FICHEIRO)== False:
        print("ficheiro não existe.")
        return False
    return True

def Adicionar():
    """função responsavel por adicionar tarefas"""
    if FicheiroExiste() == False:
        return
    
    with open(NOME_FICHEIRO,"a+",encoding="utf-8") as lista_tarefas:
        descricao = input("Insira uma breve descrição sobre a tarefa: ")
        data = input("Insira a data de conclusão da tarefa Ex:(08-05-2025): ")
        if "-" not in data:
            print("Data inserida é inválida!")
            return

        linha = descricao + " " + data
        lista_tarefas.write(linha+"\n")

def Listar():
    """função responsavel por listar as tarefas todas"""
    if FicheiroExiste() == False:
        return
    
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as lista_tarefas:
        contar = 1
        for linha in lista_tarefas:
            linha = linha.replace("\n","")
            print(contar,"-",linha)
            contar += 1

def Remover():
    """função responsavel por remover as tarefas"""
    if FicheiroExiste() == False:
        return
    
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as lista_tarefas:
        lista = lista_tarefas.readlines()

    Listar()

    remover = int(input("Insira o nº da tarefa a remover: "))
    # devido a lista ter uma posição a baixo
    remover = remover-1
    
    if remover > len(lista):
        print("Tarefa não encontrada")
        return
    else:
        del lista[remover]

    with open(NOME_FICHEIRO,"w",encoding="utf-8") as lista_tarefas:
        for linha in lista:
            lista_tarefas.write(linha)
    
    print("Removida com sucesso!")

def MarcarConcluida():
    """função responsavel por marcar a tarefa como concluida"""
    if FicheiroExiste() == False:
        return
    
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as lista_tarefas:
        lista = lista_tarefas.readlines()

    Listar()
    
    marcar = int(input("Insira o número da tarefa a concluir: "))
    if "[Concluída]" in lista[marcar-1]:
        print("Tarefa já concluida.")
        return
    
    lista[marcar-1] = "[Concluída] " + lista[marcar-1] 

    with open(NOME_FICHEIRO,"w",encoding="utf-8") as lista_tarefas:
        for linha in lista:
            lista_tarefas.write(linha)

    print(f"Tarefa número {marcar} concluída com sucesso.")
    
def ListarConcluida():
    """função responsavel por listar apenas as tarefas concluidas"""
    if FicheiroExiste() == False:
        return
    
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as lista_tarefas:
        lista = lista_tarefas.readlines()

    for linha in lista:
        if "[Concluída]" in linha:
            linha = linha.replace("\n","")
            print(linha)

def ListarMes():
    """Função para listar se a tarefa estiver no mês atual"""
    pass
    

def Menu():
    """função responsavel por gerir o menu"""
    op = 0
    while op != 7:
        op = int(input("1.Adicionar Tarefa\n2.Listar Tarefas\n3.Remover Tarefa\n4.Marcar Tarefa como concluída\n5.Listar concluídas\n6.Listar pelo mês atual\n7.Sair\nop:"))
        if op == 1:
            Adicionar()
        if op == 2:
            Listar()
        if op == 3:
            Remover()
        if op == 4:
            MarcarConcluida()
        if op == 5:
            ListarConcluida()
        if op == 6:
            ListarMes()

if __name__ == "__main__":
    Menu()