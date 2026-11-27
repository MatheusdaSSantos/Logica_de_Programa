'''Fazer um algoritmo para ler a distância percorrida em km e o total gasto de combustível, no final deverá ser exibido o consumo médio do carro.'''

distancia = float(input("Digite a distância percorrida em km: "))
combustivel = float(input("Digite o total gasto de combustível em litros: "))
consumo_medio = distancia / combustivel

print(f"O consumo médio do carro é: {consumo_medio:.2f} km/l")
