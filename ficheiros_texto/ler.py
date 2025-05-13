# para ler o ficheiro

ficheiro = open("alunos.txt","r",encoding="utf-8") 
texto= ficheiro.readline() # ou readlines para ler varias linhas e fazer lista
print(texto)
ficheiro.close()