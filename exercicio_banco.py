opcao = int(input("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))

deposito = 0
extrato = 0
extrato_de_saque = 0
saque = 0
i = 0

while opcao != 4:

    if opcao == 1:
        print("Bem Vindo(a) a área de deposito!!!\n")
        deposito = int(input("Digite o valor do deposito: \n"))
        if deposito < 0:
            print("\nVocê digitou um valor inválido\nDigite um valor positivo por favor\n")
        else:
            deposito = deposito + extrato
            extrato = deposito
            print(f"\nO deposito foi realizado com sucesso\nAgora você tem {deposito} em seu banco\n")

            opcao = int(input("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))

    if (opcao == 2) and (i != 3):
        print("\nBem vindo(a) a área de Saque!!!\n")
        print()
        saque = int(input("Digite o valor do saque: "))

        if (saque <= 0) and (saque >= 500):
            print("Valor inválido\nDigite um valor posito ou menor que R$500.00")

        elif saque > deposito:
            print(f"Valor inválido, não há dinheiro suficiente para sacar {saque} sua conta tem R${deposito}")
            opcao = int(input("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))
        else:
            deposito = deposito - saque
            print(f"Saque realizado com sucesso\nSua conta agora tem cerca de R${deposito}")
            saque = saque + extrato_de_saque
            extrato_de_saque = saque
            i = i + 1
            opcao = int(input("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))
    else:
        print("Se não tem as manhã não entra")
        opcao = int(input("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))   
        
    if opcao == 3:
        print("Bem vindo(a) a área de deposito!!!\n")
        print(f"Os seus saques foram de {extrato_de_saque}")
        print(f"Os seus depositos foram de {extrato}")
        opcao = int(input("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))

    if opcao > 4:
        print("Opção inválida")
        opcao = int(input("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Sair\n"))

    




