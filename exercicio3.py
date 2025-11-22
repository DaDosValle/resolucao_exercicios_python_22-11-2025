# Tuplas Imutáveis + Conversão Estrutural

'''Dicionários + Filtragem + Loops


Crie um programa que analise o dicionário abaixo e determine qual categoria é a mais
cara em média:
produtos = {
"Alimentação": [12.50, 8.99, 15.30],
"Limpeza": [5.20, 7.80],
"Higiene": [10.00, 12.00, 9.50, 14.00]
}
O programa deve exibir:
• categoria vencedora
• média formatada com 2 casas decimais'''


produtos = {
"Alimentação": [12.50, 8.99, 15.30],
"Limpeza": [5.20, 7.80],
"Higiene": [10.00, 12.00, 9.50, 14.00]
}




media_categoria = {}
for categoria, precos in produtos.items():
    media = sum(precos) / len(precos)
    media_categoria[categoria] = media
    
    
categoria_vencedora = max(media_categoria)

print(f'Categoria vencedora: {categoria_vencedora}')
print(f'Média: {media_categoria[categoria_vencedora]:.2f}')