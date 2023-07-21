menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:5.2f}\n"
            print(f"Operação realizada, depósito de R$ {valor:.2f}.")
        else:
            print("Operação não realizada, o valor informado é inválido")
                
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Valor informado é maior que o saldo")
        elif excedeu_limite:
            print(f"Valor maior que o limite por saque de R$ {limite:.2f}")
        elif excedeu_saques:
            print(f"Limite de saques diários ({LIMITE_SAQUES}) execedido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Operação realizada, saque de R$ {valor:.2f}.")
        
        else:
            print("Operação não realizada, o valor informado é inválido")

    elif opcao == "e":
        print("\n============EXTRATO============")
        print("Não foram realizadas operações" if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}")
        print("==============FIM===============")
       
    elif opcao == "q":
        print("Sair")
        break
    
    else:
        print("Operação inválida")
        
