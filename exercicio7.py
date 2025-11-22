'''Processamento de Dados com Loops + Dicionários Avançados

Receba uma lista de dicionários representando livros:
livros = [
{"titulo": "A", "ano": 2020, "preco": 45},
{"titulo": "B", "ano": 2024, "preco": 80},
{"titulo": "C", "ano": 2020, "preco": 50},
{"titulo": "D", "ano": 2022, "preco": 40}
]
Crie um programa que agrupe e mostre os livros por ano em ordem cronológica, exibindo
também o preço médio de cada ano.'''


from collections import defaultdict

livros = [
    {"titulo": "A", "ano": 2020, "preco": 45}, 
    {"titulo": "B", "ano": 2024, "preco": 80}, 
    {"titulo": "C", "ano": 2020, "preco": 50}, 
    {"titulo": "D", "ano": 2022, "preco": 40}
]


livros_por_ano = defaultdict(list)
for livro in livros:
    livros_por_ano[livro["ano"]].append(livro)
for ano in sorted(livros_por_ano):
    livros_ano = livros_por_ano[ano]
    preco_medio = sum(livro["preco"] for livro in livros_ano) / len(livros_ano)
    print(f"Ano: {ano}, Preço Médio: R$ {preco_medio:.2f}")
    for livro in livros_ano:
        print(f"  - {livro['titulo']}: R$ {livro['preco']}")
        