menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque = 500
numero_saques = 0
LIMITE_SAQUES = 3
movimentacoes = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            movimentacoes.append(f'Depósito: R$ {valor_deposito:.2f}')
            print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso.')
        else:
            print("Valor de depósito inválido.")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: R$ "))
        if valor_saque > 0 and valor_saque <= limite_saque:
            if saldo >= valor_saque and numero_saques < LIMITE_SAQUES:
                saldo -= valor_saque
                movimentacoes.append(f'Saque: R$ {valor_saque:.2f}')
                numero_saques += 1
                print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso.')
            elif numero_saques >= LIMITE_SAQUES:
                print("Você atingiu o limite de saques diários.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido.")

    elif opcao == "e":
        if not movimentacoes:
            print('Não foram realizadas movimentações.')
        else:
            print('Extrato:')
            for movimento in movimentacoes:
                print(movimento)
            print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
   