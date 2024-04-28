### DESAFIO ###
# """ 1- Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu python. Para a primeira versão do sistema devemos implementar apenas 3 operações:
# 	1.1- depósito: Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# 	2- saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# 	3- extrato: Essa operação deve listar todos depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx.
# 	EX.: 1500.45 = R$ 1500.45 """

menu = """
         SEJA BEM-VINDO AO BANCO D.I.O                    
    Por favor nós informe o que deseja fazer:

    [D] Depósito
    [S] Sacar
    [E] Extrato Bancário
    [Q] Sair

=> """
deposito = 0
saldo = 0
limite = 500
numero_saque = 0
extrato = ""
LIMITE_SAQUE = 3

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Qual o valor que você deseja depósitar? "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!!")
        else:
            print(f"\nOperação falhou, valor informardo não permitido. ")

    elif opcao == "S":
        valor = float(input("Informe o valor que deseja para o saque? "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            print("\nRetire o seu dinheiro na boca do caixa")

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "Q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
