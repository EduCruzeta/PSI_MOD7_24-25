import csv

# lista vazia para guardar os dados do ficheiro
dados = []

# abrir o ficheiro para leitura
with open("ficheiro.csv","r",encoding="utf-8") as ficheiro:
    # criar o objeto para ler o csv
    ler = csv.DictReader(ficheiro)

    # ler cada linha do ficheiro e adicionar a lista
    for linha in ler:
        dados.append(linha)

print(dados)