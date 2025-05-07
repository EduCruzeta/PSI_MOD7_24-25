""" 
O programa vai ler uma frase em ingles do utilizador depois verifica se as palavras estão no dicionario
"""
import os

NOME_FICHEIRO = "words.txt"

def FicheiroExiste():
    if os.path.exists(NOME_FICHEIRO)== False:
        print("Dicionário não existe.")
        return False
    return True

def LerFrase():
    """Função para ler uma frase do utilizador e devolver uma lista de palavras"""
    texto = input("Introduza uma frase: ")
    texto = texto.strip().lower()
    #TODO testar oque acontece se a frase só tiver uma palavra
    return texto.split(" ")

def LerFicheiro():
    """Função para ler todas as linhas de um ficheiro de texto e devolver uma lista"""
    with open(NOME_FICHEIRO,"r",encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
    # converter todas as palavras do dicionário para minusculas
    for i in range(len(linhas)):
        linhas[i] = linhas[i].lower()
    return linhas    

def Verificar(palavras,dicionario):
    """Função recebe as palavras a verificar e a lista de palavras do dicionário.
      Mostra as palavras que não existem no dicionário ou uma mensagem de não existencia de erros."""
    erro = False
    for palavra in palavras:
        # adicionar \n para a comparação funcionar
        if palavra+"\n" not in dicionario:
            print(f"A palavra {palavra} não existe ou está errada.")
            erro = True
    if erro == False:
        print("A frase não tem erros")

def main():
    if FicheiroExiste() == False:
        print("Não existe ficheiro do dicionário.")
        return
    palavras = LerFrase()
    dicionario = LerFicheiro()
    Verificar(palavras,dicionario)

if __name__=="__main__":
    main()