lista = []
while True:
    valor = input("Diegite um valor: ").lower()
    if valor == "fim":
        break
    lista.append(*int(valor))
lista1 = [3*i for i in lista]
print(lista1)    
