from controleFinanceiro import controleFinanceiro

print("*******Controle de Transações***********")
print("")
print("1 - Cadastrar nova transação")
print("2 - Listar transações cadastradas")
print("3 - Sair")
print("")
opc = int(input("Escolha uma das operações acima:"))

if opc == 1:
    descrição = input("Forneça uma descrição da nova transção:")
    valor = float(input("informe o valor da transação:"))
    tipo = input("Tipo da transação:")
    movimentacao = Transacao(descricao,valor,tipo)
    meu_Gerenciador.adicionaTransacao(movimentacao)

if opc == 2:
    meu_Gerenciador.listarTransacoes()