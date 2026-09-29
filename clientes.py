from colorama import init, Fore

init(autoreset=True)


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        print(Fore.GREEN + "\n" + "-" * 40)
        print(Fore.GREEN + "       CLIENTE CADASTRADO")
        print(Fore.GREEN + "-" * 40)

        print(Fore.WHITE + f"\nNome: {self.nome}")
        print(Fore.WHITE + f"E-mail: {self.email}")
        print(Fore.WHITE + f"Telefone: {self.telefone}")

        print(Fore.GREEN + "\nCadastro realizado com sucesso.")
        print(Fore.GREEN + "-" * 40)


def validar_nome(nome):
    return (
        all(caractere.isalpha() or caractere.isspace() for caractere in nome)
        and nome.strip()
    )


def validar_email(email):
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    return usuario != "" and "." in dominio


def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) >= 8


def carregar_clientes():
    clientes = []

    try:
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split("|")

                if len(dados) == 3:
                    cliente = Cliente(dados[0], dados[1], dados[2])
                    clientes.append(cliente)

    except FileNotFoundError:
        pass

    return clientes


def salvar_cliente(cliente):
    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(
            f"{cliente.nome}|{cliente.email}|{cliente.telefone}\n"
        )


def cadastrar_cliente():
    print(Fore.YELLOW + "\n" + "-" * 40)
    print(Fore.YELLOW + "         CADASTRO DE CLIENTE")
    print(Fore.YELLOW + "-" * 40)

    while True:
        nome = input(Fore.WHITE + "Nome: ")

        if validar_nome(nome):
            break

        print(
            Fore.RED
            + "Nome inválido! Digite apenas letras e espaços."
        )

    while True:
        email = input(Fore.WHITE + "E-mail: ")

        if validar_email(email):
            break

        print(
            Fore.RED
            + "E-mail inválido! Exemplo: nome@email.com"
        )

    while True:
        telefone = input(Fore.WHITE + "Telefone: ")

        if validar_telefone(telefone):
            break

        print(
            Fore.RED
            + "Telefone inválido! Digite apenas números."
        )

    cliente = Cliente(
        nome.title(),
        email.lower(),
        telefone
    )

    salvar_cliente(cliente)
    cliente.exibir_dados()

    return cliente