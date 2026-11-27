nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
media = (nota1 + nota2) / 2

print(f"Média: {media:.1f}")


if media >= 9:

    print("Você está de parabéns.")

elif media >= 7:

    print("Você está aprovado")

elif media >= 5:

    print("Você está de reuperação.")

elif media >= 1:

    print("Você precisa estudar mais no próximo ano.")

else:
    print("Você está reprovado.")
