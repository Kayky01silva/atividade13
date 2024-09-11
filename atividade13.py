# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.


def verificar_numero(numero):
    if numero > 0:
        return "O número é positivo."
    elif numero < 0:
        return "O número é negativo."
    else:
        return "O número é zero."

try:
    numero = float(input("Digite um número: "))
    
    resultado = verificar_numero(numero)
    print(resultado)
except ValueError:
    print("Por favor, digite um número válido.")
