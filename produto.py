
from colorama import Fore, Style, init

init()

try:
    nome = input("Digite o nome do produto: ").strip()

    if nome == "":
        print(Fore.RED + "Erro: O nome do produto não pode ser vazio." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Nome cadastrado com sucesso!" + Style.RESET_ALL)

except ValueError:
    print(Fore.RED + "Erro: O nome do produto não pode ser vazio." + Style.RESET_ALL)


try:
    preco = float(input("Digite o preço do produto: "))

    if preco < 0:
        print(Fore.RED + "Erro: O preço do produto não pode ser negativo." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Preço cadastrado com sucesso!" + Style.RESET_ALL)

except ValueError:
    print(Fore.RED + "Erro: O preço do produto deve ser um NÚMERO válido." + Style.RESET_ALL)


try:
    quantidade = int(input("Digite a quantidade do produto: "))

    if quantidade < 0:
        print(Fore.RED + "Erro: A quantidade do produto não pode ser negativa." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Quantidade cadastrada com sucesso!" + Style.RESET_ALL)

except ValueError:
    print(Fore.RED + "Erro: A quantidade do produto deve ser um NÚMERO válido." + Style.RESET_ALL)


print(Fore.CYAN + "\n--- Cadastro do Produto ---" + Style.RESET_ALL)
print(f"Nome: {nome}")
print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")

