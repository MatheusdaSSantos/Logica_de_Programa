"""Uma empresa paga R$10.00 por hora normal trabalhada e R$ 15.00 por hora extra. Escreva um algoritmo que 
leia o total de horas normais trabalhadas e o total de horas extras trabalhadas por um empregado em um ano 
e calcule o salário anual deste trabalhador.
Exemplo : Entrada :  Digite o número de horas trabalhadas no ano : 1760
Digite o número de horas extras trabalhadas no ano : 400
Saída :    Seu salário anual é de : R$ 23600"""

horas_normais = float(input("Digite o número de horas trabalhadas no ano: "))
horas_extras = float(input("Digite o número de horas extras trabalhadas no ano: "))

salario_normal = horas_normais * 10.00
salario_extra = horas_extras * 15.00
salario_anual = salario_normal + salario_extra

print(f"Seu salário anual é de : R$ {salario_anual:.2f}")
