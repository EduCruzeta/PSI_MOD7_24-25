
"""
tipos de abertura de abertura de ficheiros EX: ficheiro =open("alunos.txt","r")
r - Leitura
w - Escrever/Destruir tudo do ficheiro caso exista
a - Escrever no final do ficheiro
r+ - Leitura/Escrever
w+ - Leitura/Escrever(cria ficheiro)
a+ - Leitura/Escrever(no final)
fechar o ficheiro - ficheiro.close()
"""

ficheiro = open("alunos.txt","w",encoding="utf-8") #<- para codificar strings
ficheiro.write("Olá mundo\n")
ficheiro.write("Fim")
ficheiro.close()

with open("alunos.txt","w",encoding="utf-8") as ficheiro: # usado para nao ser obrigatorio fechar o programa 
    ficheiro.write("Olá mundo\n")
    ficheiro.write("Fim")



