"""Criar um algoritmo para ler um tempo em segundos e fazer a impressão no console no seguinte formato:
hora:minuto:segundos"""

segundos_totais = int(input("Digite o tempo em segundos: "))

horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60
segundos = segundos_totais % 60

print(f"{horas}:{minutos}:{segundos}")
