from colorama import init, Fore

init(autoreset=True)


def carregar_produtos():
    produtos = []

    try:
        with open("produtos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split("|")

                if len(dados) == 3:
                    nome = dados[0]
                    preco = float(dados[1])
                    quantidade = int(dados[2])

                    produtos.append(
                        {
                            "nome": nome,
                            "preco": preco,
                            "quantidade": quantidade
                        }
                    )

    except FileNotFoundError:
        pass

    return produtos


def salvar_produto(nome, preco, quantidade):
    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{nome}|{preco}|{quantidade}\n"
        )


def cadastrar_produto():
    print(Fore.CYAN + "\n" + "-" * 40)
    print(Fore.CYAN + "         SISTEMA DE PRODUTOS")
    print(Fore.CYAN + "-" * 40)
    print(Fore.WHITE + "Informe os dados do produto abaixo.\n")

    while True:
        nome = input(Fore.WHITE + "Nome do produto: ").strip()

        if nome:
            break

        print(
            Fore.RED
            + "O nome do produto não pode ser vazio.\n"
        )

    while True:
        try:
            preco = float(
                input(Fore.WHITE + "Preço do produto: R$ ")
            )

            if preco > 0:
                break

            print(
                Fore.RED
                + "O preço deve ser maior que zero.\n"
            )

        except ValueError:
            print(
                Fore.RED
                + "Digite um valor numérico válido.\n"
            )

    while True:
        try:
            quantidade = int(
                input(Fore.WHITE + "Quantidade: ")
            )

            if quantidade > 0:
                break

            print(
                Fore.RED
                + "A quantidade deve ser maior que zero.\n"
            )

        except ValueError:
            print(
                Fore.RED
                + "Digite uma quantidade válida.\n"
            )

    salvar_produto(nome, preco, quantidade)

    print(Fore.GREEN + "\n" + "-" * 40)
    print(Fore.GREEN + "       PRODUTO CADASTRADO")
    print(Fore.GREEN + "-" * 40)

    print(Fore.WHITE + f"\nNome: {nome}")
    print(Fore.WHITE + f"Preço: R$ {preco:.2f}")
    print(Fore.WHITE + f"Quantidade: {quantidade}")

    print(Fore.GREEN + "\nCadastro realizado com sucesso.")
    print(Fore.GREEN + "-" * 40)

    return {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }