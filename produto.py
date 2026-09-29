from colorama import init, Fore

# Inicializa o Colorama
init(autoreset=True)

print(Fore.CYAN + "\n" + "-" * 40)
print(Fore.CYAN + "         SISTEMA DE PRODUTOS")
print(Fore.CYAN + "-" * 40)
print(Fore.WHITE + "Informe os dados do produto abaixo.\n")


# Cadastro do nome
while True:
    nome = input(Fore.WHITE + "Nome do produto: ").strip()

    if nome:
        break

    print(Fore.RED + "O nome do produto não pode ser vazio.\n")


# Cadastro do preço
while True:
    try:
        preco = float(input(Fore.WHITE + "Preço do produto: R$ ").replace(",", "."))

        if preco > 0:
            break

        print(Fore.RED + "O preço deve ser maior que zero.\n")

    except ValueError:
        print(Fore.RED + "Digite um valor numérico válido.\n")


# Cadastro da quantidade
while True:
    try:
        quantidade = int(input(Fore.WHITE + "Quantidade: "))

        if quantidade > 0:
            break

        print(Fore.RED + "A quantidade deve ser maior que zero.\n")

    except ValueError:
        print(Fore.RED + "Digite uma quantidade válida.\n")


# Exibição dos dados
print(Fore.GREEN + "\n" + "-" * 40)
print(Fore.GREEN + "       PRODUTO CADASTRADO")
print(Fore.GREEN + "-" * 40)

print(Fore.WHITE + f"\nNome: {nome}")
print(Fore.WHITE + f"Preço: R$ {preco:.2f}")
print(Fore.WHITE + f"Quantidade: {quantidade}")

print(Fore.GREEN + "\nCadastro realizado com sucesso.")
print(Fore.GREEN + "-" * 40)