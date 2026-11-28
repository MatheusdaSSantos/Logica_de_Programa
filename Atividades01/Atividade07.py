"""Sistema de folha de pagamento
Uma empresa deseja calcular o salário de seus funcionários.

Solicite:
Nome do funcionário.
Salário-base.
Quantidade de horas extras.
Valor da hora extra.

Calcule:
Total de horas extras.
Salário bruto.
Desconto de 8% referente ao INSS (valor didático simplificado).
Vale Transporte 6%
Salário líquido.
Apresente todos os valores formatados com duas casas decimais."""

nome = input("Nome do funcionário: ")
salario_base = float(input("Salário-base: R$ "))
qtd_horas_extras = float(input("Quantidade de horas extras: "))
valor_hora_extra = float(input("Valor da hora extra: R$ "))

total_horas_extras = qtd_horas_extras * valor_hora_extra
salario_bruto = salario_base + total_horas_extras

desconto_inss = salario_bruto * 0.08
vale_transporte = salario_bruto * 0.06
salario_liquido = salario_bruto - desconto_inss - vale_transporte

print("\n===== FOLHA DE PAGAMENTO =====")
print(f"Funcionário: {nome}")
print(f"Salário-base: R$ {salario_base:.2f}")
print(f"Total de horas extras: R$ {total_horas_extras:.2f}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
print(f"Vale Transporte (6%): R$ {vale_transporte:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
