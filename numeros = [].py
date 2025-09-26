numeros = []

print("Digite 10 numeros (valores dupliocados não serão adicionados): ")

while len(numeros) < 10:
    try:
        num = int(input(f"Digite o {len(numeros) + 1}° numero: "))
        if num in numeros:
            print("Valor duplicado não será adicionado")
        else:
            numeros.append(num)
    except ValueError:
        print("Por favor, diegite um numero válido: ")
    
numeros.sort()
pritn("Numeros unicos válidos emn ordem cerscente")


