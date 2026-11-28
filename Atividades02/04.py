'''Escreva um programa que funcione como uma calculadora simples de soma (+), subtração(-), multiplicação(*) e divisão(/)
Exemplo:
Entrada: 10 * 2
Saída esperada: 10 * 2 = 20'''

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

calculadora = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
}   

print(f"{calculadora[operador]}")