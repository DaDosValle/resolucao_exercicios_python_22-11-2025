# 1. Listas + Compreensão de Listas + Condicionais


'''Dada uma lista de números inteiros, crie um programa que gere duas listas novas.
• uma contendo apenas os números primos
• outra contendo os números não primos'''

numeros_eh_par = []
numeros_eh_impar = []


numero = int(input("Insira um número inteiro (ou digite -0 para terminar): "))


while numero != -0:

    if numero % 2 == 0:

        numeros_eh_par.append(numero)
    else:

        numeros_eh_impar.append(numero)
    numero = int(input("Insira outro número inteiro (ou digite -0 para terminar): "))


print("\n--- Resultados ---")
print("Números pares coletados:", numeros_eh_par)
print("Números ímpares coletados:", numeros_eh_impar)