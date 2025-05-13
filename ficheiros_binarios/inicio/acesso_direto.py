"""
Programa para ler os dados de um registro com base no nº do registo
Cada registro ocupa 28 bytes (20sif -> nnome,idade,saldo)
"""
import os, struct

TAMANHO_REGISTRO = 28
# calcular o tamanho do ficheiro
tamanho_ficheiro = os.path.getsize("dados.bin")
# calcular o nº de registros

numero_registros = tamanho_ficheiro / TAMANHO_REGISTRO
print(f"{tamanho_ficheiro}-{numero_registros}")

numero_a_ler = int(input(f"Tem {int(numero_registros)} para ler qual o que pretende? "))

if numero_a_ler > numero_registros:
    print("Não existe esse registro")
else:
    # abrir o ficheiro para leitura 
    with open("dados.bin","rb") as ficheiro:
        # posicionar o cursor no byte correspondente ao registo a ler
        byte_ler = (numero_a_ler -1) * TAMANHO_REGISTRO
        ficheiro.seek(byte_ler)
        # ler o registo
        dados_binarios = ficheiro.read(28)
        # faz o desempacotamento
        dados = struct.unpack("20sif",dados_binarios)
        print(dados[0].decode("utf-8").rstrip("\x00"))
        print(dados[1])
        print(dados[2])

