# 2 Tuplas Imutáveis + Conversão Estrutural

'''Você recebe uma lista de tuplas contendo (nome, nota) de alunos.
Crie um programa que:
• transforme os dados em um dicionário
• se o aluno já existir, calcule a média das notas recebidas
• exiba os alunos em ordem crescente de média
Exemplo de entrada:
[("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]'''


alunos_notas = []

while True:
    entrada = input("Digite o nome do aluno e sua nota. Ex: nome, nota (separados por vírgula) ou 'sair' para finalizar: ")
    if entrada.lower() == 'sair':
        break
    else:
        nome, nota = entrada.split(',')
        alunos_notas.append((nome.strip(), int(nota.strip())))


notas_por_aluno = {}
for nome, nota in alunos_notas:
    if nome in notas_por_aluno:
        notas_por_aluno[nome].append(nota)
    else:
        notas_por_aluno[nome] = [nota]


medias = {nome: sum(notas)/len(notas) for nome, notas in notas_por_aluno.items()}


def obter_media(item):
    return item[1]

for nome, media in sorted(medias.items(), key=obter_media):
    print(f"{nome}: {media:.2f}")
