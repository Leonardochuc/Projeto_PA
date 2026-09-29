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
print(colorama.Fore.CYAN + "\n--- Cadastro do Produto ---" + colorama.Style.RESET_ALL)
print(f"Nome: {nome}")
print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")