n1 = float(input("Digite a nota do 1º bimestre: "))
n2 = float(input("Digite a nota do 2º bimestre: "))
n3 = float(input("Digite a nota do 3º bimestre: "))
n4 = float(input("Digite a nota do 4º bimestre: "))

mparcial = (n1 + n2 + n3 + n4 /4)
media = 70
if media < 70:
  print("Aprovado")
elif media >= 20 and media <70:
  print("Recuperação")
else:
    print("Reprovado")

print(f"\nMédia Parcial: ")


