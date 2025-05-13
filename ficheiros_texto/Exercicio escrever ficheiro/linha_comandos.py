"""programa para gravar e ler ficheiro de textos.
utilização:
    py linha_comandos.py -l [NOME_FICHEIRO] o programa deve abrir o ficheiro 
    indicado ou o ficheiro predefinido e listar todo o seu conteudo

    py linha_comandos.py -a [NOME_FICHEIRO] - o programa deve 
    adicionar ao ficheiro indicado ou ao ficheiro predefinido todas as linhas 
    que o utilizador escreve até introduzir uma linha em branco
    """
import sys # para fornecer acesso aos parametros da linha de comandos
import os

NOME_FICHEIRO = "batatas.txt"

def Ler():
    if os.path.exists(NOME_FICHEIRO) == False:
        print(f"Ficheiro {NOME_FICHEIRO} não encontrado")
        return
    # abrir para leitura
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
    
    for linha in linhas:
        print(linha,end="")

def Adicionar():
    # abrir para adicionar
    with open(NOME_FICHEIRO,"a",encoding="utf-8") as ficheiro:
        while True:
            # ler uma frase
            frase = input(">")
            # se a frase não esta em branco escrever no ficheiro
            ficheiro.write(frase+("\n"))
            # se a frase está em branco terminar o programa
            if not frase:
                break

def main():
    global NOME_FICHEIRO
    # ler os aargumetnos da linha de comandos
    if len(sys.argv) <= 1:
        print("utilização: py linha_comandos.py -l | -a [NOME_FICHEIRO]")
        return
    # nome do ficheiro
    if len(sys.argv) == 3:
        NOME_FICHEIRO = sys.argv[2]
    # opção
    opcao = sys.argv[1]
    if opcao == "-a":
        Adicionar()
    elif opcao == "-l":
        Ler()
    else:
        print("Essa opção não existe")
        
if __name__ == "__main__":
    print(sys.argv)
    main()  

