'''Biblioteca Externa (collections) + Contagem
Usando Counter da biblioteca collections, escreva um programa que receba uma frase do
usuário e exiba:
• o 3° caractere mais frequente
• e quantas vezes ele aparece
Caso hajam empates ou menos de 3 caracteres únicos, trate adequadamente com
mensagens claras.'''

   
    
    
from collections import Counter

frase = input("Digite uma frase: ")

caracteres_limpos = []
for char in frase.lower():

    if not char.isspace():
        caracteres_limpos.append(char)


caracteres_contados = Counter(caracteres_limpos)
mais_comuns = caracteres_contados.most_common()


if len(mais_comuns) < 3:
    print("\nAVISO: A frase não contém 3 caracteres únicos (após remover os espaços).")

    if len(mais_comuns) > 0:
        print(f"O caractere mais comum é '{mais_comuns[0][0]}' e aparece {mais_comuns[0][1]} vezes.")
    
else:
   
    terceiro_mais_comum = mais_comuns[2]
    
    char_exibido = terceiro_mais_comum[0]
    contagem = terceiro_mais_comum[1]
    
    print("-" * 40)
    print(f"O 3° caractere mais frequente é '{char_exibido}'")
    print(f"Ele aparece {contagem} vezes.")