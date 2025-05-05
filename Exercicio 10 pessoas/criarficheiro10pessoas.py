with open("pessoas.txt","w",encoding="utf-8") as ficheiro: 
    for i in range(10):
        nome = input("insira o seu nome: ")
        ficheiro.write(nome)
        ficheiro.write("\n")