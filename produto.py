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
        print(colorama.Fore.RED + "Erro: O preço deve ser um número válido." + colorama.Style.RESET_ALL)
# Cadastro da quantidade
while True:
    try:
        quantidade = int(input("Digite a quantidade do produto: "))

        if quantidade < 0:
            print(colorama.Fore.RED + "Erro: A quantidade não pode ser negativa." + colorama.Style.RESET_ALL)
        else:
            print(colorama.Fore.GREEN + "Quantidade cadastrada com sucesso!" + colorama.Style.RESET_ALL)
            break

    except ValueError:
        print(colorama.Fore.RED + "Erro: A quantidade deve ser um número inteiro válido." + colorama.Style.RESET_ALL)


