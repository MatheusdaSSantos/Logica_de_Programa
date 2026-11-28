'''Escreva um programa que encontre o valor máximo entre 2 números
Exemplo:
Entrada:
Digite um número: 2
Digite outro número: 1

Saída:
O número 2 é maior que o número 1'''

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}")
else:
    print(f"O número {num2} é maior que o número {num1}")
