# Sistema Bancário em Python

Este é um projeto simples de um sistema bancário em Python que permite a criação de clientes, contas bancárias, e a realização de transações básicas como depósitos, saques e exibição de extratos.

## Funcionalidades

- **Criar Cliente:** Cadastro de um novo cliente.
- **Criar Conta:** Criação de uma nova conta para um cliente existente.
- **Depositar:** Realizar um depósito em uma conta.
- **Sacar:** Realizar um saque de uma conta.
- **Extrato:** Exibir o extrato de uma conta.
- **Listar Contas:** Listar todas as contas criadas.

## Estrutura do Projeto

O projeto é composto pelas seguintes classes principais:

- `Cliente`: Representa um cliente do banco, com endereço e contas associadas.
- `PessoaFisica`: Subclasse de `Cliente`, adiciona informações específicas de uma pessoa física como nome, data de nascimento e CPF.
- `Conta`: Representa uma conta bancária genérica.
- `ContaCorrente`: Subclasse de `Conta`, adiciona funcionalidades específicas de uma conta corrente como limite de saque e número máximo de saques.
- `Historico`: Mantém o histórico de transações de uma conta.
- `Transacao`: Classe abstrata para uma transação bancária.
- `Saque`: Subclasse de `Transacao`, representa uma operação de saque.
- `Deposito`: Subclasse de `Transacao`, representa uma operação de depósito.

## Como Usar

1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/sistema-bancario.git
    cd sistema-bancario
    ```

2. **Execute o Script:**

    ```bash
    python sistema_bancario.py
    ```

3. **Interaja com o Menu:**

    Após executar o script, você verá um menu com as opções disponíveis. Siga as instruções na tela para realizar as operações desejadas.

## Exemplo de Uso

1. **Criar um Novo Cliente:**

    - Selecione a opção `NU` no menu.
    - Insira o CPF, nome completo, data de nascimento e endereço do cliente.

2. **Criar uma Nova Conta:**

    - Selecione a opção `NC` no menu.
    - Insira o CPF do cliente existente.

3. **Realizar um Depósito:**

    - Selecione a opção `D` no menu.
    - Insira o CPF do cliente e o valor do depósito.

4. **Realizar um Saque:**

    - Selecione a opção `S` no menu.
    - Insira o CPF do cliente e o valor do saque.

5. **Exibir Extrato:**

    - Selecione a opção `E` no menu.
    - Insira o CPF do cliente para visualizar o extrato da conta.

6. **Listar Contas:**

    - Selecione a opção `LC` no menu para listar todas as contas.

## Notas

- O sistema não implementa persistência de dados. Todas as informações são armazenadas em memória e serão perdidas ao encerrar o programa.
- Certifique-se de inserir valores válidos ao realizar operações para evitar erros.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato através do email: seu-email@example.com