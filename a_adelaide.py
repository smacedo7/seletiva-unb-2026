# Problema A - Adelaide

# Leia uma frase e imprima:
# - a frase original;
# - "Para que?";
# - "PARAGUAY!".

# Entrada:
# Uma string de 10 a 100 caracteres.

# Saída:
# Frase original seguida de:
# Para que?
# PARAGUAY!


# Resolução:
frase = input("")
if len(frase) >= 10 and len(frase) <= 100:
    print(f'{frase}')
    print("Para que?")
    print("PARAGUAY!")
