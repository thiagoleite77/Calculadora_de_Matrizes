def ler_matriz(nome):
    linhas = int(input(f"\nNúmero de linhas da Matriz {nome}: "))
    colunas = int(input(f"Número de colunas da Matriz {nome}: "))

    matriz = []
    print(f"\nDigite os valores da Matriz {nome}:")
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            while True:
                try:
                    val = float(input(f"Posição [{i + 1},{j + 1}]: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, insira um número.")
            linha.append(val)
        matriz.append(linha)

    return matriz, linhas, colunas

def mostrar_matriz(matriz, linhas, colunas):
    for i in range(linhas):
        print("| ", end='')
        for j in range(colunas):
            print(f"{matriz[i][j]:6.2f} ", end='')
        print("|")

def somar_matrizes(matrizA, matrizB, linhas, colunas):
    print("\n=== Soma de Matrizes ===")
    resultado = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            val = matrizA[i][j] + matrizB[i][j]
            print(f"Posição [{i + 1},{j + 1}]: {matrizA[i][j]} + {matrizB[i][j]} = {val}")
            linha.append(val)
        resultado.append(linha)
    return resultado

def subtrair_matrizes(matrizA, matrizB, linhas, colunas):
    print("\n=== Subtração de Matrizes ===")
    resultado = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            val = matrizA[i][j] - matrizB[i][j]
            print(f"Posição [{i + 1},{j + 1}]: {matrizA[i][j]} - {matrizB[i][j]} = {val}")
            linha.append(val)
        resultado.append(linha)
    return resultado
def multiplicar_por_escalar(matriz, linhas, colunas, escalar):
    print("\n=== Multiplicação por Escalar ===")
    resultado = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            val = matriz[i][j] * escalar
            print(f"Posição [{i + 1},{j + 1}]: {escalar} × {matriz[i][j]} = {val}")
            linha.append(val)
        resultado.append(linha)
    return resultado

def multiplicar_matrizes(matrizA, matrizB, linhasA, colunasA, colunasB):
    print("\n=== Multiplicação de Matrizes ===")
    resultado = []
    for i in range(linhasA):
        linha = []
        for j in range(colunasB):
            soma = 0
            print(f"\nCalculando posição [{i + 1},{j + 1}]:")
            for k in range(colunasA):
                produto = matrizA[i][k] * matrizB[k][j]
                soma += produto
                print(f"  {matrizA[i][k]} × {matrizB[k][j]} = {produto}")
            print(f"Soma = {soma}")
            linha.append(soma)
        resultado.append(linha)
    return resultado

def transpor_matriz(matriz, linhas, colunas):
    print("\n=== Matriz Transposta ===")
    resultado = []
    for i in range(colunas):
        linha = []
        for j in range(linhas):
            val = matriz[j][i]
            print(f"Posição [{j + 1},{i + 1}] -> [{i + 1},{j + 1}]: {val}")
            linha.append(val)
        resultado.append(linha)
    return resultado, colunas, linhas  # troca linhas/colunas

# Programa principal
matrizA, matrizB = [], []
linhasA = colunasA = 0
linhasB = colunasB = 0

while True:
    print("\n=== Calculadora de Matrizes ===")
    print("1 - Ler Matriz A")
    print("2 - Ler Matriz B")
    print("3 - Somar Matrizes (A + B)")
    print("4 - Subtrair Matrizes (A - B)")
    print("5 - Multiplicar por Escalar")
    print("6 - Multiplicar Matrizes (A x B)")
    print("7 - Calcular Transposta")
    print("8 - Mostrar Matrizes")
    print("9 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida! Digite um número de 1 a 9.")
        continue

    match opcao:
        case 1:
            matrizA, linhasA, colunasA = ler_matriz("A")
        case 2:
            matrizB, linhasB, colunasB = ler_matriz("B")
        case 3:
            if linhasA != linhasB or colunasA != colunasB:
                print("\nERRO: As matrizes precisam ter as mesmas dimensões para soma!")
            else:
                resultado = somar_matrizes(matrizA, matrizB, linhasA, colunasA)
                print("\nResultado:")
                mostrar_matriz(resultado, linhasA, colunasA)
        case 4:
            if linhasA != linhasB or colunasA != colunasB:
                print("\nERRO: As matrizes precisam ter as mesmas dimensões para subtração!")
            else:
                resultado = subtrair_matrizes(matrizA, matrizB, linhasA, colunasA)
                print("\nResultado:")
                mostrar_matriz(resultado, linhasA, colunasA)
        case 5:
            try:
                escalar = float(input("Digite o valor do escalar: "))
            except ValueError:
                print("Entrada inválida! Deve ser um número.")
                continue
            escolha = input("Qual matriz deseja multiplicar? (A/B): ").upper()
            if escolha == 'A' and linhasA > 0:
                resultado = multiplicar_por_escalar(matrizA, linhasA, colunasA, escalar)
                mostrar_matriz(resultado, linhasA, colunasA)
            elif escolha == 'B' and linhasB > 0:
                resultado = multiplicar_por_escalar(matrizB, linhasB, colunasB, escalar)
                mostrar_matriz(resultado, linhasB, colunasB)
            else:
                print("Escolha inválida ou matriz não definida.")
        case 6:
            if colunasA != linhasB:
                print("\nERRO: O número de colunas de A deve ser igual ao número de linhas de B!")
            else:
                resultado = multiplicar_matrizes(matrizA, matrizB, linhasA, colunasA, colunasB)
                print("\nResultado:")
                mostrar_matriz(resultado, linhasA, colunasB)
        case 7:
            escolha = input("Qual matriz deseja transpor? (A/B): ").upper()
            if escolha == 'A' and linhasA > 0:
                resultado, linhasR, colunasR = transpor_matriz(matrizA, linhasA, colunasA)
                mostrar_matriz(resultado, linhasR, colunasR)
            elif escolha == 'B' and linhasB > 0:
                resultado, linhasR, colunasR = transpor_matriz(matrizB, linhasB, colunasB)
                mostrar_matriz(resultado, linhasR, colunasR)
            else:
                print("Escolha inválida ou matriz não definida.")
        case 8:
            if linhasA > 0:
                print("\nMatriz A:")
                mostrar_matriz(matrizA, linhasA, colunasA)
            if linhasB > 0:
                print("\nMatriz B:")
                mostrar_matriz(matrizB, linhasB, colunasB)
        case 9:
            print("Saindo...")
            break
        case _:
            print("Opção inválida! Tente novamente.")
