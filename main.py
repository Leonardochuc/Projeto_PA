from clientes import cadastrar_cliente, carregar_clientes
from produto import cadastrar_produto, carregar_produtos


clientes = carregar_clientes()
produtos = carregar_produtos()


print("\n" + "=" * 40)
print("       SISTEMA DE CADASTRO")
print("=" * 40)

print(f"\nClientes carregados: {len(clientes)}")
print(f"Produtos carregados: {len(produtos)}")


while True:
    print("\n" + "-" * 40)
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar produto")
    print("3 - Sair")
    print("-" * 40)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cliente = cadastrar_cliente()
        clientes.append(cliente)

    elif opcao == "2":
        produto = cadastrar_produto()
        produtos.append(produto)

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida. Escolha 1, 2 ou 3.")