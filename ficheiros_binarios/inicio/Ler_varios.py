"""
Programa para ler dados de um ficheiro binário com o formato:
nome  - 20s
idade - i
saldo - f
------------
        28 bytes
"""
import struct

with open("dados.bin","rb") as ficheiro:
    # ler os dados todos de uma só vez
    dados_binarios = ficheiro.read(28)
    dados = struct.unpack("20sif",dados_binarios)

# converter a string binaria numa string
nome = dados[0].decode("utf-8").rstrip("\x00")
print(f" Nome:{nome} Idade:{dados[1]} Saldo:{dados[2]}")