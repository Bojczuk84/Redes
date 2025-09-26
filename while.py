lista = []
for i in range(10):
    valor = int(input("Digite um valor: "))
    if not valor in lista:
        lista.append(valor)

        print(sorted(lista))