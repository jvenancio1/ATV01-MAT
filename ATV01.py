# Funções para verificar semelhança de triângulos
def verifica_lal(lados1, lados2, angulo1, angulo2):
    proporcao_lados = lados1[0] / lados2[0] == lados1[1] / lados2[1]
    angulos_congruentes = angulo1 == angulo2
    return proporcao_lados and angulos_congruentes

def verifica_aa(angulos1, angulos2):
    return sorted(angulos1) == sorted(angulos2)

def verifica_lll(lados1, lados2):
    proporcao_1_2 = lados1[0] / lados2[0]
    proporcao_2_3 = lados1[1] / lados2[1]
    proporcao_3_1 = lados1[2] / lados2[2]
    return proporcao_1_2 == proporcao_2_3 == proporcao_3_1

# Função principal para verificar a semelhança dos triângulos
def verifica_seme_lhanca_triangulos():
    tipo = input("Escolha o critério de semelhança (LAL, AA, LLL): ").upper()
    
    if tipo == "LAL":
        lados1 = list(map(float, input("Digite os dois lados do primeiro triângulo (separados por espaço): ").split()))
        lados2 = list(map(float, input("Digite os dois lados do segundo triângulo (separados por espaço): ").split()))
        angulo1 = float(input("Digite o ângulo entre os lados do primeiro triângulo: "))
        angulo2 = float(input("Digite o ângulo entre os lados do segundo triângulo: "))
        if verifica_lal(lados1, lados2, angulo1, angulo2):
            print("Os triângulos são semelhantes pelo critério LAL.")
        else:
            print("Os triângulos não são semelhantes pelo critério LAL.")
    
    elif tipo == "AA":
        angulos1 = list(map(float, input("Digite os dois ângulos do primeiro triângulo (separados por espaço): ").split()))
        angulos2 = list(map(float, input("Digite os dois ângulos do segundo triângulo (separados por espaço): ").split()))
        if verifica_aa(angulos1, angulos2):
            print("Os triângulos são semelhantes pelo critério AA.")
        else:
            print("Os triângulos não são semelhantes pelo critério AA.")
    
    elif tipo == "LLL":
        lados1 = list(map(float, input("Digite os três lados do primeiro triângulo (separados por espaço): ").split()))
        lados2 = list(map(float, input("Digite os três lados do segundo triângulo (separados por espaço): ").split()))
        if verifica_lll(lados1, lados2):
            print("Os triângulos são semelhantes pelo critério LLL.")
        else:
            print("Os triângulos não são semelhantes pelo critério LLL.")
    
    else:
        print("Critério inválido.")

# Executa a função principal
verifica_seme_lhanca_triangulos()
