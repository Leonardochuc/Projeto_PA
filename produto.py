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
            print(Fore.RED + "Erro: O preço do produto não pode ser negativo." + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Preço cadastrado com sucesso!" + Style.RESET_ALL)
            break

    except ValueError:
        print(Fore.RED + "Erro: O preço deve ser um número válido." + Style.RESET_ALL)

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
        print(colorama.Fore.RED + "Erro: A quantidade deve ser um número inteiro válido." + colorama.Styleama.Style.RESET_ALL)

# Exibição do cadastro
print(Fore.CYAN + "\n--- Cadastro do Produto ---" + Style.RESET_ALL)
print(f"Nome: {nome}")
print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
