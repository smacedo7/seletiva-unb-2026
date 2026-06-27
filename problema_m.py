# Problema M - Maior

# Dado um inteiro positivo n, encontre o maior número que pertence à
# interseção entre:
# - o conjunto dos divisores de n (positivos e negativos);
# - o conjunto dos números ímpares positivos.

# Entrada:
# Um inteiro n.

# Saída:
# O maior divisor ímpar positivo de n.

# resoluçao errada, visto que execuçao vai levar 2 bilhões de iterações
def maior(n):
    divisores = set()
    impares = set()

    for i in range(-n, n + 1):
        if i != 0:
            if n % i == 0:
                # daria pra resolver tudo num if n % i == 0 and if i % 2 != 0
                divisores.add(i)
            if i % 2 != 0:
                impares.add(i)
    return max(divisores.intersection(impares))


n = int(input(""))
print(maior(n))

# fator 2 faz o numero ser par. Se tirá-lo, fator impar maior vai ser o maior
# divisor. Exemplo:
# 72 -> 2, 2, 2, 3, 3
# tirando fatores par: 72 -> 3, 3 = 3^3 = 9
# maior divisor impar = 9

# resoluçao certa, O(log n)
numero = int(input(''))

while True:
    if numero % 2 == 0:
        numero //= 2
    else:
        break
print(numero)