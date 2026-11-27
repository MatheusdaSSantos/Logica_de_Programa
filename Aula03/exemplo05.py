idade = int(input("Digite a idade:"))
resposta = "Maior de idade" if idade >= 18 else "Menor de Idade"
print(resposta)

a = 10
b = 5
maior = a if a > b else b
print(f"Maior número:{maior}")

nota = 8
situacao = (
    "Aprovado com Louvor" if nota >= 9 else "Aprovado" if nota >= 7 else "Reprovado"
)
print(situacao)

if True:
    print("Imprima algo")
    print("teste")

ativo = True
if not ativo:
    print("inativado")
else:
    print("O recurso está ok")
