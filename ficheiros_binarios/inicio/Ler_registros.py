"""
Programa para ler varios registros do ficheiro.
Cada registro tem 28 bytes (20sif -> nnome,idade,saldo)

"""
import struct

with open("dados.bin","rb") as ficheiro:
    while True:
        try:
            # ler os dados todos de uma só vez
            dados_binarios = ficheiro.read(28)
            if not dados_binarios:
                break
            dados = struct.unpack("20sif",dados_binarios)
            # converter a string binaria numa string
            nome = dados[0].decode("utf-8").rstrip("\x00")
            print(f" Nome:{nome} Idade:{dados[1]} Saldo:{dados[2]}")
        except EOFError:
            break