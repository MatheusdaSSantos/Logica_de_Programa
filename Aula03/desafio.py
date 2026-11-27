nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
media = (nota1 + nota2) / 2

print(f"Média: {media:.1f}")


def nova_funcao(media):
    match True:
        case _ if media >= 9:
            print("Você está de parabéns.")
        case _ if media >= 7:
            print("Você está aprovado")
        case _ if media >= 5:
            print("Você está de recuperação.")
        case _ if media >= 1:
            print("Você precisa estudar mais no próximo ano.")
        case _:
            print("Você está reprovado.")


nova_funcao(media)