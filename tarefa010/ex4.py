IPI = float(input("Digite a porcentagem do IPI: "))

codigo_peca1 = input("Digite o código da primeira peça: ")
valor_peca1 = float(input("Digite o valor da primeira peça: "))
quantidade_peca1 = int(input("Digite a quantidade da primeira peça: "))

codigo_peca2 = input("Digite o código da segunda peça: ")
valor_peca2 = float(input("Digite o valor da segunda peça: "))
quantidade_peca2 = int(input("Digite a quantidade da segunda peça: "))

valor_total = (valor_peca1 * quantidade_peca1 + valor_peca2 * quantidade_peca2) * (IPI / 100 + 1)
print("O valor total a ser pago é:", valor_total)