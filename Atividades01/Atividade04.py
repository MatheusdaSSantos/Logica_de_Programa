'''Criar um algoritmo que leia dois números inteiros e imprima a seguinte saída:
Dividendo, Divisor, Quociente e Resto'''

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")
