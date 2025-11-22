'''Listas + Loop + Operações Matemáticas

Implemente uma função que receba dois vetores (listas) de igual tamanho e retorne o
produto escalar entre eles, sem usar bibliotecas externas.
Exemplo:
A = [2, 3, 5]
B = [1, 4, 2]
→ Saída: 2*1 + 3*4 + 5*2 = 24'''

A = [2, 3, 5]
B = [1, 4, 2]



def produto_escalar(vetor_a, vetor_b):
    if len(vetor_a) != len(vetor_b):
        print("Os vetores devem ter o mesmo tamanho.")
    
    resultado = 0
    for a, b in zip(vetor_a, vetor_b):
        resultado += a * b
    
    return resultado


resultado =produto_escalar(A, B)
print(resultado) 