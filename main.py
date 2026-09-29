while True:
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastro de cliente")
    print("2 - Cadastro de produto")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nAbrindo cadastro de cliente...")
        exec(open("clientes.py", encoding="utf-8").read())

    elif opcao == "2":
        print("\nAbrindo cadastro de produto...")
        exec(open("produto.py", encoding="utf-8").read())

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida. Escolha 1, 2 ou 3.")