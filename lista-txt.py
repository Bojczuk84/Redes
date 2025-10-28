def main():
    pessoas = [] 
    print("Digite o nome e o email das pessoas. Para encerrar, digite 'END' no nome.\n")

    while True:
        nome = input("Nome: ").strip()
        if nome.upper() == "END":
            break
        email = input("Email: ").strip()

        pessoas.append([nome, email])

    with open("pessoas.txt", "w", encoding="utf-8") as arquivo:
        for pessoa in pessoas:
            linha = f"{pessoa[0]},{pessoa[1]}\n"
            arquivo.write(linha)

    print("\nDados salvos com sucesso em 'pessoas.txt'!")
    print("Conteúdo salvo:")
    for pessoa in pessoas:
        print(f"{pessoa[0]} - {pessoa[1]}")

if __name__ == "__main__":
    main()