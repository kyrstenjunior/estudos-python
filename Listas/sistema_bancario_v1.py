from datetime import datetime, timedelta

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
VALOR_LIMITE_TRANSACOES = 2
mascara_ptbr = "%d/%m/%Y %H:%M"
data_atual = datetime.now()
historico_transacoes = {}

def adicionar_transacao(data, operacao, valor):
    global historico_transacoes
    global VALOR_LIMITE_TRANSACOES

    index = len(historico_transacoes)
    historico_transacoes[index + 1] = {"data": data, "transação": f"{operacao} | R$ {valor:.2f}"}
    VALOR_LIMITE_TRANSACOES -= 1

def transacoes():
    global historico_transacoes
    for valor in historico_transacoes.values():
        print(valor)

# Extrato
def imprimir_extrato():
    global extrato
    return print(f"\n{extrato}Saldo disponível: R$ {saldo:.2f}")

# Depositar
def depositar(valor):
    global saldo
    global extrato
    global VALOR_LIMITE_TRANSACOES
    valor = float(valor)

    if(valor > 0 and VALOR_LIMITE_TRANSACOES > 0):
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        adicionar_transacao(data_atual.strftime(mascara_ptbr), "DEPÓSITO", valor)
        return print("Depósito realizado com sucesso!")
    elif(valor < 0):
        return "Digite um valor maior do que 0..."
    else:
        print("Limite de transações diárias excedido! Tente novamente amanhã...")
        return transacoes()

# Sacar
def sacar(valor):
    global saldo
    global extrato
    global limite_saques
    global VALOR_LIMITE_SAQUE
    global VALOR_LIMITE_TRANSACOES

    valor = float(valor)

    if(valor <= saldo and valor <= VALOR_LIMITE_SAQUE and limite_saques > 0 and VALOR_LIMITE_TRANSACOES > 0):
        saldo -= valor
        limite_saques -= 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        adicionar_transacao(data_atual.strftime(mascara_ptbr), "SAQUE", valor)
        print("\nSaque realizado com sucesso!\n")
        return print(f"Saques disponíveis: {limite_saques}\n")
    elif valor > saldo:
        print("O saque falhou!\n")
        return print(f"\nO valor solicitado é maior do que o disponível em sua conta. Digite um valor menor.\nSaques disponíveis: {limite_saques}\n")
    elif valor > VALOR_LIMITE_SAQUE:
        print("O saque falhou!\n")
        return print(f"\nO limite de saque é de R$ {VALOR_LIMITE_SAQUE}/saque. Digite um valor menor.\nSaques disponíveis: {limite_saques}\n")
    elif VALOR_LIMITE_TRANSACOES <= 0:
        print("O saque falhou!\n")
        print("Limite de transações diárias excedido! Tente novamente amanhã...")
        transacoes()
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