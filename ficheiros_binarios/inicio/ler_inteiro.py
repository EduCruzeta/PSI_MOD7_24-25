"""
Ler um número inteiro do ficheiro binário
"""
import struct

with open("int.dat","rb") as ficheiro:
    numero = struct.unpack("i",ficheiro.read(4))

print(numero[0])