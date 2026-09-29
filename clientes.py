from colorama import init, Fore

# Inicializa o Colorama
init(autoreset=True)


class Cliente:
    def _init_(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        print(Fore.GREEN + "\n✓ Cliente cadastrado com sucesso!")
        print(Fore.CYAN + "=" * 30)
        print(Fore.CYAN + f"Nome: {self.nome}")
        print(Fore.CYAN + f"E-mail: {self.email}")
        print(Fore.CYAN + f"Telefone: {self.telefone}")
        print(Fore.CYAN + "=" * 30)


def validar_nome(nome):
    return all(caractere.isalpha() or caractere.isspace() for caractere in nome) and nome.strip()


def validar_email(email):
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")

    return usuario != "" and "." in dominio


def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) >= 8


print(Fore.YELLOW + "=" * 35)
print(Fore.YELLOW + "      CADASTRO DE CLIENTE")
print(Fore.YELLOW + "=" * 35)
