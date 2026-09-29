import colorama

colorama.init()

# Cadastro do nome
while True:
    nome = input("Digite o nome do produto: ").strip()

    if nome == "":
        print(colorama.Fore.RED + "Erro: O nome do produto não pode ser vazio." + colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.GREEN + "Nome cadastrado com sucesso!" + colorama.Style.RESET_ALL)
        break


# Cadastro do preço
while True:
    try:
        preco = float(input("Digite o preço do produto: "))

        if preco < 0:
            print(colorama.Fore.RED + "Erro: O preço do produto não pode ser negativo." + colorama.Style.RESET_ALL)
        else:
            print(colorama.Fore.GREEN + "Preço cadastrado com sucesso!" + colorama.Style.RESET_ALL)
            break

    except ValueError:
        print(colorama.Fore.RED + "Erro: O preço do produto deve ser um NÚMERO válido." + colorama.Style.RESET_ALL)


# Exibição do cadastro print(colorama.Fore.CYAN + "\n--- Cadastro do Produto ---" + colorama.Style.RESET_ALL) print(f"Nome: {nome}") print(f"Preço: R$ {preco:.2f}") print(f"Quantidade: {quantidade}")