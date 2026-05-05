# Cálculo de produtividade
#-------------------------

print('===Cálculo de Produtividade===')

try:
    total_produzido = float(input('Valor total da venda:'))
    funcionarios = int(input('Total de funcionários:'))


    media_por_funcionarios = total_produzido / funcionarios
    print(f'Média por Funcionário:{media_por_funcionarios:.2f}') 
except ValueError:
    print('Informe um número.')
except ZeroDivisionError :
    print('Funcionário não pode ser Zero.')
    