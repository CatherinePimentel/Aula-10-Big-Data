# Programa que simula um caixa eletrônico 

print("===Caixa Eletrônico===")

try:
    saldo = 1000
    saque = float(input('Insira um valor:'))

except ValueError:
    print('Valor inválido:')

except KeyboardInterrupt:
    print('Programa encerrado pelo usuário')
else:
    if saque > saldo:
        print('Saldo insuficiente')
    elif saque <= 0:
        print('Saque precisa ser maior ou igual a R$ 2,00')
    else:
        saldo -= saque 
        print('\nSaque realizado com sucesso')
        print(f'Saldo em conta R${saldo:.2f}')
finally:
    print('Operação realizada')
    





