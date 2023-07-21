def menu():
    menu = """\n
    ==============MENU==============    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [q] Sair
    =================================
    \n===> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:5.2f}\n"
            print(f"Operação realizada, depósito de R$ {valor:.2f}.")
    else:
        print("Operação não realizada, o valor informado é inválido")

    return saldo, extrato

                
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):       
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Valor informado é maior que o saldo disponível.")
        elif excedeu_limite:
            print(f"Valor maior que o limite por saque de R$ {limite:.2f}.")
        elif excedeu_saques:
            print(f"Limite de saques diários ({limite_saques}) execedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Operação realizada, saque de R$ {valor:.2f}.")
        
        else:
            print("Operação não realizada, o valor informado é inválido")

        return saldo, extrato 

    
def exibir_extrato(saldo, /, *, extrato):
    print("\n============EXTRATO============")
    print("Não foram realizadas operações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============FIM================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (apenasnq números)): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Este usuário já existe!")
        return

    nome = input("Informe o seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o seu endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(f"\nUsuário {nome} criado com sucesso!") 

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o seu CPF (apenasnq números)): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"Agência: {agencia} e C/C: {numero_conta} criados.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuarios}
    
    print("Usuário não encontrado, não foi possível criar uma nova conta.")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    AGENCIA = "0001"
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques,

            )
        
        elif opcao == "nu":
             criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = conta =+ 1 
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(numero_conta)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
   
        elif opcao == "q":
            print("Sair")
            break
        
        else:
            print("Operação inválida")
            
main()