# Eliabe de Jesus e Fábio Ferreira

import random, os

def f_campo(tamanho:int)->list:
    campo = []

    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            n = random.randint(1, 5)
            if  (n % 2 == 1):
                linha.append("Vazio")
            else:
                linha.append("Mina")
        campo.append(linha)
    
    return campo
#------------------------------------------------
def f_revelacao(campo:list, m:list)->bool:
    linha = int(input("Digite o número da linha: ")) - 1
    coluna = int(input("Digite o número da coluna: ")) - 1
    os.system("cls")

    if ((linha, coluna) in m):
        m.remove((linha, coluna))
    
    if (0 <= linha < len(campo) and 0 <= coluna < len(campo[0])):
        if (campo[linha][coluna] == "Vazio" or campo[linha][coluna] == "Revelado"):
            print("Você encontrou uma célula vazia!")
            campo[linha][coluna] = "Revelado"
            print(f'Há {f_adjacente(campo, linha, coluna)} mina(s) nas proximidades!')
            return True
        else:
            os.system("cls")
            f_imprimeCampoPerdedor(campo)
            print("Você encontrou uma mina! Game Over!")
            return False
    print("Posição inválida! Tente novamente.")
    return True
#------------------------------------------------
def f_adjacente(campo:list, linha:int, coluna:int)->int:
    minas = []

    if  (linha == 0):
        if (coluna == 0):
            minas.append(campo[linha][coluna + 1])
            minas.append(campo[linha + 1][coluna])
            minas.append(campo[linha + 1][coluna + 1])
        elif (coluna == len(campo[0]) - 1):
            minas.append(campo[linha][coluna - 1])
            minas.append(campo[linha + 1][coluna - 1])
            minas.append(campo[linha + 1][coluna])
        else:
            minas.append(campo[linha][coluna - 1])
            minas.append(campo[linha][coluna + 1])
            minas.append(campo[linha + 1][coluna - 1])
            minas.append(campo[linha + 1][coluna])
            minas.append(campo[linha + 1][coluna + 1])
    elif (linha == len(campo) - 1):
        if (coluna == 0):
            minas.append(campo[linha][coluna + 1])
            minas.append(campo[linha - 1][coluna])
            minas.append(campo[linha - 1][coluna + 1])
        elif (coluna == len(campo[0]) - 1):
            minas.append(campo[linha][coluna - 1])
            minas.append(campo[linha - 1][coluna - 1])
            minas.append(campo[linha - 1][coluna])
        else:
            minas.append(campo[linha][coluna - 1])
            minas.append(campo[linha][coluna + 1])
            minas.append(campo[linha - 1][coluna - 1])
            minas.append(campo[linha - 1][coluna])
            minas.append(campo[linha - 1][coluna + 1])
    else:
        if (coluna == 0):
            minas.append(campo[linha][coluna + 1])
            minas.append(campo[linha - 1][coluna])
            minas.append(campo[linha + 1][coluna])
            minas.append(campo[linha - 1][coluna + 1])
            minas.append(campo[linha + 1][coluna + 1])
        elif (coluna == len(campo[0]) - 1):
            minas.append(campo[linha][coluna - 1])
            minas.append(campo[linha - 1][coluna - 1])
            minas.append(campo[linha + 1][coluna - 1])
            minas.append(campo[linha - 1][coluna])
            minas.append(campo[linha + 1][coluna])
        else:
            minas.append(campo[linha][coluna - 1])
            minas.append(campo[linha][coluna + 1])
            minas.append(campo[linha - 1][coluna - 1])
            minas.append(campo[linha - 1][coluna])
            minas.append(campo[linha - 1][coluna + 1])
            minas.append(campo[linha + 1][coluna - 1])
            minas.append(campo[linha + 1][coluna])
            minas.append(campo[linha + 1][coluna + 1])

    return minas.count("Mina")
#------------------------------------------------
def f_marcacao(campo:list)->tuple:
    linha = int(input("Escreva o número da linha da célula supeita: ")) - 1
    coluna = int(input("Escreva o nome da coluna da célula suspeita: ")) - 1
    os.system("cls")

    if (0 <= linha < len(campo) and 0 <= coluna < len(campo[coluna]) and campo[linha][coluna] != "Revelado"):
        return (linha, coluna)
#------------------------------------------------
def f_vencedor(campo:list)->bool:
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            if (campo[i][j] == "Vazio"):
                return False
    return True
#------------------------------------------------
def f_imprimeCampo(campo:list, marcacao:list)->None:
    for i in range(len(campo) + 1):
        if (i == len(campo)):
            print(i)
        else:
            print(i, end=" ")
    
    for i in range(len(campo)):
        print(i + 1, end=" ")
        for j in range(len(campo[i])):
            if ((i, j) in marcacao):
                print("M", end=" ")
            elif (campo[i][j] == "Vazio" or campo[i][j] == "Mina"):
                print("X", end=" ")
            else:
                valor = f_adjacente(campo, i, j)
                print(valor, end=" ")
        print()
#------------------------------------------------
def f_imprimeCampoVencedor(campo:list)->None:
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            if (campo[i][j] == "Mina"):
                print("B", end=" ")
            else:
                print("R", end=" ")
        print()
#------------------------------------------------
def f_imprimeCampoPerdedor(campo:list)->None:
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            if (campo[i][j] == "Mina"):
                print("B", end=" ")
            else:
                print("R", end=" ")
        print()
#------------------------------------------------
def main():
    t = int(input("Digite o tamanho do campo: "))
    campo = f_campo(t)
    game = True
    m = []
    os.system("cls")

    while game:
        f_imprimeCampo(campo, m)
        print("#------------------------------------------------")
        print("1 - Marcar suspeita")
        print("2 - Marcar célula")
        opcao = int(input("Digite sua opção: "))
        os.system("cls")

        f_imprimeCampo(campo, m)
        print("#------------------------------------------------")
        if (opcao == 1):
            m.append(f_marcacao(campo))
        elif (opcao == 2):
            game = f_revelacao(campo, m)

        if (f_vencedor(campo)):
            os.system("cls")
            f_imprimeCampoVencedor(campo)
            print("Parabéns, você ganhou!")
            break


if __name__== "__main__":
    main()
