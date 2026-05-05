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
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário')
else:
    print(f'Média por funcionário: {media_por_funcionarios}')
# Executa sempre. Com erro ou não , o bloco finally sempre ir executar

finally:
    print('Programa encerrado!')
    