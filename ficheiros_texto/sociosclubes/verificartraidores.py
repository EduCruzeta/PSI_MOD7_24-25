""" O programa vai abrir 2 ficheiros e verificar nomes iguais em ambos"""

academico = open("academico.txt","r",encoding="utf-8")
tondela = open("tondela.txt","r",encoding="utf-8")

lista_academico = academico.readlines()
lista_tondela = tondela.readlines()

for academista in lista_academico:
    for tondelista in lista_tondela:
        if academista == tondelista:
            print(f"Encontrou um intruzo nome-> {academista}")

academico.close()
tondela.close()
