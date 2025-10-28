def main():
    pessoas = []

    try:
        with open("pessoas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
            
                dados = linha.strip().split(",")
                if len(dados) == 2:
                    pessoas.append(dados)

        print("Dados restaurados com sucesso!\n")
        print("Lista reconstruída:")
        print(pessoas)

    except FileNotFoundError:
        print("Erro: O arquivo 'pessoas.txt' não foi encontrado. Execute o primeiro script antes.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")


if __name__ == "__main__":
    main()