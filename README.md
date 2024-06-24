### Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python, que permite realizar operações básicas como depósito, saque, exibição de extrato, criação de usuário e contas, e listagem de contas.

#### Funcionalidades Implementadas:

- **Depositar:** Permite adicionar um valor ao saldo da conta.
- **Sacar:** Permite retirar um valor do saldo da conta, considerando limite de saques e saldo disponível.
- **Extrato:** Exibe um resumo das operações realizadas e o saldo atual da conta.
- **Nova Conta:** Cria uma nova conta associada a um usuário existente.
- **Listar Contas:** Mostra informações detalhadas de todas as contas criadas.
- **Novo Usuário:** Registra um novo usuário com CPF único.

#### Estrutura do Programa:

O sistema está estruturado em diversas funções que interagem para fornecer as funcionalidades mencionadas. Aqui está uma visão geral das principais partes do código:

- **Menu de Opções:**
  - O menu permite ao usuário selecionar a operação desejada utilizando abreviações de comandos.
  - As operações incluem depósito, saque, exibição de extrato, criação de usuário, criação de conta e listagem de contas.

- **Funções Principais:**
  - `menu()`: Exibe o menu ao usuário e retorna a opção escolhida.
  - `depositar(saldo, valor, extrato)`: Realiza a operação de depósito e atualiza o saldo e o extrato da conta.
  - `sacar(saldo, valor, extrato, limite, numero_saques, limite_saques)`: Realiza a operação de saque verificando saldo, limite e número de saques.
  - `exibir_extrato(saldo, extrato)`: Exibe um resumo das transações realizadas e o saldo atual.
  - `criar_usuario(usuarios)`: Registra um novo usuário no sistema, solicitando informações como CPF, nome, data de nascimento e endereço.
  - `filtrar_usuario(cpf, usuarios)`: Filtra um usuário existente pelo CPF.
  - `criar_conta(agencia, numero_conta, usuarios)`: Cria uma nova conta associada a um usuário existente, após informar o CPF do usuário.
  - `listar_contas(contas)`: Mostra detalhes de todas as contas criadas, incluindo agência, número da conta e nome do titular.

- **Execução Principal:**
  - O programa principal (`main()`) gerencia o fluxo de execução, chamando as funções apropriadas de acordo com a opção selecionada pelo usuário.

#### Execução do Programa:

Para executar o programa, basta rodar o script Python. O sistema continuará em execução até que o usuário escolha a opção de sair (`Q`).

```python
def main():
    # Inicialização de variáveis
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # Loop principal do programa
    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "Q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
```

### Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este sistema bancário, sinta-se à vontade para fazer um fork do repositório, implementar suas melhorias e enviar um pull request.

### Autor

Este sistema bancário em Python foi desenvolvido por [Luiz Eduardo](https://github.com/edufrannca).
