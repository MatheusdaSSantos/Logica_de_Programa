"""Escreva um programa que leia a temperatura em Celsius e retorne o valor em Fahrenheit
F = C x 1,8 + 32
Para que você consiga converter de grau Celsius para Fahrenheit, basta multiplicar a temperatura em graus Celsius por 1,8 e somar 32.

Exemplo:

37º C para Fahrenheit:
F = 37 x 1,8 + 32;
F = 98,6;
37 graus Celsius equivalem a 98,6 graus Fahrenheit."""

temperatura = float(input("Digite o valor em Cº: "))

Fahrenheit = temperatura * 1.8 + 32

print(f"A temperatura em Fahrenheit é de: {Fahrenheit:.2f}")
