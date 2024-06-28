def realizar_deposito(deposito, extrato):
    valor_deposito = int(input("Digite o valor do depósito: "))
    if valor_deposito < 0:
        print("\nVocê digitou um valor inválido. Digite um valor positivo, por favor.\n")
    else:
        deposito += valor_deposito
        extrato = deposito
        print(f"\nO depósito foi realizado com sucesso. Agora você tem R${deposito} em sua conta.\n")
    return deposito, extrato

def realizar_saque(deposito, extrato_de_saque, i):
    saque = int(input("Digite o valor do saque: "))
    if saque <= 0 or saque >= 500:
        print("Valor inválido. Digite um valor positivo ou menor que R$500.00.")
    elif saque > deposito:
        print(f"Valor inválido. Não há dinheiro suficiente para sacar R${saque}. Sua conta tem R${deposito}.")
    else:
        deposito -= saque
        print(f"Saque realizado com sucesso. Sua conta agora tem cerca de R${deposito}.")
        extrato_de_saque += saque
        i += 1
    return deposito, extrato_de_saque, i

def exibir_extrato(extrato, extrato_de_saque):
    print("\nBem-vindo(a) à área de extrato!!!")
    print(f"Os seus saques foram de R${extrato_de_saque}")
    print(f"Os seus depósitos foram de R${extrato}")

def main():
    deposito = 0
    extrato = 0
    extrato_de_saque = 0
    i = 0

    while True:
        print("1 - Depósito\n2 - Saque\n3 - Extrato\n4 - Sair\n")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            deposito, extrato = realizar_deposito(deposito, extrato)
        elif opcao == 2 and i != 3:
            deposito, extrato_de_saque, i = realizar_saque(deposito, extrato_de_saque, i)
        elif opcao == 3:
            exibir_extrato(extrato, extrato_de_saque)
        elif opcao == 4:
            print("Saindo do programa. Obrigado!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
