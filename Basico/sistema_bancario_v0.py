menu = """

[1] Extrato
[2] Depositar
[3] Sacar
[4] Sair

=> """

saldo = 2000
limite_saques = 3
extrato = ""
VALOR_LIMITE_SAQUE = 500

# Extrato
def imprimir_extrato():
    global extrato
    return print(f"\n{extrato}Saldo disponível: R$ {saldo:.2f}")

# Depositar
def depositar(valor):
    global saldo
    global extrato
    valor = float(valor)

    if(valor > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return print("Depósito realizado com sucesso!")
    else:
        return "Digite um valor maior do que 0..."

# Sacar
def sacar(valor):
    global saldo
    global extrato
    global limite_saques
    global VALOR_LIMITE_SAQUE

    valor = float(valor)

    if(valor <= saldo and valor <= VALOR_LIMITE_SAQUE and limite_saques > 0):
        saldo -= valor
        limite_saques -= 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("\nSaque realizado com sucesso!\n")
        return print(f"Saques disponíveis: {limite_saques}\n")
    elif valor > saldo:
        print("O saque falhou!\n")
        return print(f"\nO valor solicitado é maior do que o disponível em sua conta. Digite um valor menor.\nSaques disponíveis: {limite_saques}\n")
    elif valor > VALOR_LIMITE_SAQUE:
        print("O saque falhou!\n")
        return print(f"\nO limite de saque é de R$ {VALOR_LIMITE_SAQUE}/saque. Digite um valor menor.\nSaques disponíveis: {limite_saques}\n")
    elif limite_saques == 0:
        print("O saque falhou!\n")
        return print(f"\nLimite de saques diários esgotado. Volte amanhã!")

while True:
    opcao = input(menu)

    if opcao == "1":
        imprimir_extrato()
    elif opcao == "2":
        valor_operacao = input("\nQual valor deseja depositar? R$ ")
        depositar(valor_operacao)
    elif opcao == "3":
        valor_operacao = input("\nQual valor deseja sacar? R$ ")
        sacar(valor_operacao)
    elif opcao == "4":
        break
    else:
        print("Operação inválida, tente novamente...")