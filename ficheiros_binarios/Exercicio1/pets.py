"""
Programa para gerir uma loja de animais com ficheiros binarios
"""
import os,struct

NOME_FICHEIRO = "pets.bin"
TAMANHO_REGISTRO = 39

def FicheiroExiste():
    if os.path.exists(NOME_FICHEIRO)== False:
        print("ficheiro não existe.")
        return False
    return True

def Adicionar():
    """Função responsavel por adicionar os animais ao ficheiro binário"""
    # ler dados do animal
    raca = input("Insira a raça do animal: ")
    if len(raca) > 30:
        print("Raça invalida tem que ser menor que 30 caracteres.")
        return
    peso = float(input("Insira o peso do animal: "))
    genero = input("Insira o gereno do animal Ex:(m/f)")
    preco = float(input("Insira o preço do animal: "))
    
    with open(NOME_FICHEIRO,"+ab") as ficheiro:
        # empacotar os dados todos
        # raça
        dados_empacotados = struct.pack("30s",raca.encode("utf-8"))
        ficheiro.write(dados_empacotados)
        # Peso
        dados_empacotados = struct.pack("f",peso)
        ficheiro.write(dados_empacotados)
        # gênero
        dados_empacotados = struct.pack("1s",genero.encode("utf-8"))
        ficheiro.write(dados_empacotados)
        # Preço
        dados_empacotados = struct.pack("f",preco)
        ficheiro.write(dados_empacotados)
        print("Dados registrados com sucesso!")
        
def Listar_todos():
    "Função responsavel por listar todos os animais do ficheiro"

    if FicheiroExiste() == False:
        return
    
    with open(NOME_FICHEIRO,"rb") as ficheiro:
        while True:
            # raça
            dados_binario = ficheiro.read(30)
            if not dados_binario:
                break
            dados = struct.unpack("30s",dados_binario)
            raca = dados[0].decode("utf-8").rstrip("\x00")
            # peso
            dados_binario = ficheiro.read(4)
            dados = struct.unpack("f",dados_binario)
            peso = dados[0]
            # genero
            dados_binario = ficheiro.read(1)
            dados = struct.unpack("1s",dados_binario)
            genero = dados[0].decode("utf-8").rstrip("\x00")
            # preço
            dados_binario = ficheiro.read(4)
            dados = struct.unpack("f",dados_binario)
            preco = dados[0]
            print("|\|----------------------------------------------------------------------------------|\|")
            print(f"Raça: {raca} |-| Peso:{round(peso)} |-| Gênero:{genero} |-| Preço:{round(preco)}€")
            print("|\|----------------------------------------------------------------------------------|\|")

def Apagar():
    """
    Lista os pets e perguntar qual deseja apagar
    """
    with open(NOME_FICHEIRO,"rb") as f_ler:
        # criar um ficheiro temporário
        with open("temp.bin","wb") as f_escrever:
            while True:
                raca_binaria = f_ler.read(30)
                if not raca_binaria:
                    break
                # ler um registro
                peso_binaria = f_ler.read(4)
                genero_binaria = f_ler.read(1)
                preco_binaria = f_ler.read(4)
                raca = struct.unpack("30s",raca_binaria)
                # mostrar ao utilizar
                print("Raça: ",raca[0].decode("utf-8").rstrip("\x00"))
                # se NÂO é para apagar gravar no ficheiro temp
                op = input("Pretende apagar s/n: ")
                if op not in "sS":
                    f_escrever.write(raca_binaria)
                    f_escrever.write(peso_binaria)
                    f_escrever.write(genero_binaria)
                    f_escrever.write(preco_binaria)
    # apagar o ficheiro temp
    os.remove(NOME_FICHEIRO)
    # mudar o nome do ficheiro temporario
    os.rename("temp.bin",NOME_FICHEIRO)
    print("Animal removido com sucesso")

def Editar():
    """Lista os pets e pergunta qual quer editar"""
    # Abrir o ficheiro para leitura e escrita
    with open(NOME_FICHEIRO,"rb+") as ficheiro:
        # ler um registro 
        while True:
            raca_binaria = ficheiro.read(30)
            if not raca_binaria:
                break  # terminar o ciclo porque chegou ao final do ficheiro
            peso_binaria = ficheiro.read(4)
            genero_binaria = ficheiro.read(1)
            preco_binaria = ficheiro.read(4)
            # mostrar ao utilizador
            raca = struct.unpack("30s",raca_binaria)[0]
            raca = raca.decode("utf-8").rstrip("\x00")
            peso = struct.unpack("f",peso_binaria)[0]
            genero = struct.unpack("1s",genero_binaria)[0]
            genero = genero.decode("utf-8").rstrip("\x00")
            preco = struct.unpack("f",preco_binaria)[0]
            print(f"{raca} - {peso} - {genero} - {preco}")
            op = input("op?: ")
            # perguntar se quer alterar
            if op in "sS":
                raca = input("Nova raça: ")
                if len(raca) > 30:
                    print("Raça invalida tem que ser menor que 30 caracteres.")
                    return
                peso = float(input("Novo peso: "))
                genero = input("Novo genero do animal Ex:(m/f): ")
                preco = float(input("Novo preço do animal: "))
                # se alterar gravar novamente o mesmo registro
                ficheiro.seek(-39,os.SEEK_CUR)
                ficheiro.write(struct.pack("30s",raca.encode("utf-8")))
                ficheiro.write(struct.pack("f",peso))
                ficheiro.write(struct.pack("1s",genero.encode("utf-8")))
                ficheiro.write(struct.pack("f",preco))

def Menu():
        op = 0
        while op != 5:
            print("1.Adicionar\n2.Listar\n3.Apagar\n4.Editar\n5.Sair")
            op = int(input("op:"))
            if op == 1:
                Adicionar()
            if op == 2:
                Listar_todos()
            if op == 3:
                Apagar()
            if op == 4:
                Editar()
            if op == 5:
                break

if __name__ == "__main__":
    Menu()