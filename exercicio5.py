'''Condicionais + Tratamento de Erros

Faça um programa que receba um número digitado pelo usuário e:
• verifique se pode ser convertido para float
• caso não possa, exiba uma mensagem de erro personalizada
• se o número for válido:
o se for decimal (ex.: 2.5), exiba sua parte inteira e decimal
o se for inteiro, informe se é par ou ímpar'''

def verificar_numero():
    entrada = input("Digite um número: ")
    try:
        numero = float(entrada)
        if numero.is_integer():
            numero_inteiro = int(numero)
            if numero_inteiro % 2 == 0:
                print(f"O número {numero_inteiro} é inteiro e par.")
            else:
                print(f"O número {numero_inteiro} é inteiro e ímpar.")
        else:
            parte_inteira = int(numero)
            parte_decimal = numero - parte_inteira
            print(f"O número {numero} é decimal. Parte inteira: {parte_inteira}, Parte decimal: {parte_decimal}")
    except ValueError:
        print("Erro: A entrada não é um número válido.")

verificar_numero()