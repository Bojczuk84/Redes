numeros = []

print("Digite 10 números (valores duplicados não serão adicionados):")

while len(numeros) < 10:
    try:
        num = int(input(f"Digite o {len(numeros) + 1}º número: "))
        if num in numeros:
            print("Valor duplicado! Não será adicionado.")
        else:
            numeros.append(num)
    except ValueError:
        print("Por favor, digite um número válido.")

numeros.sort()
print("\nNúmeros únicos digitados em ordem crescente:")
print(numeros)
