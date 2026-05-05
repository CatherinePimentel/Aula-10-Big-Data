print('===Cálculo de Produtividade===')

try:
    total_produzido = float(input('Valor total da venda:'))
    funcionarios = int(input('Total de funcionários:'))
    media_por_funcionario = total_produzido / funcionarios
    
    
except Exception as e:
    print(f'Ops! Erro nos valores de entrada{e}')
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário')
else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')

# Executa sempre. Com erro ou não , o bloco finally sempre ir executar

finally:
    print('Programa encerrado!')
    