with open("alunos.txt","r",encoding="utf-8") as ficheiro: 
    texto = ficheiro.readline()
    print(texto)
    ficheiro.seek(0) # para ir ao inicio do ficheiro
    texto = ficheiro.readline()
    print(texto)
