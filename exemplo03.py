print('===Cálculo de Produtividade===')

try:
    total_produzido = float(input('Valor total da venda:'))
    funcionarios = int(input('Total de funcionários:'))
    


    media_por_funcionarios = total_produzido / funcionarios
    print(f'Média por Funcionário:{media_por_funcionarios:.2f}') 
except (ValueError, TypeError):
    print('O valor precisa ser numérico.')
except ZeroDivisionError :
    print('Funcionário não pode ser Zero.')
else :
    print(f'Média por Funcionário:{media_por_funcionarios:.2f}')
    