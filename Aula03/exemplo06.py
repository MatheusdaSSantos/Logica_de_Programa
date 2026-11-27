hora = int(input("Digite a hora (0-23): "))
if hora < 0 or hora > 23:
    print("Hora inválida. Digite um valor entre 0 e 23.")
elif hora >= 8 and hora <= 12:
    print("Horario comercial")
elif hora >= 13 and hora <= 14:
    print("Horario almoco!")
elif hora >= 15 and hora <= 18:
    print("Horario comercial")
else:
    print("Fora horario comercial")
