ano = int(input('Digite um determinado ano: '))
ano_bissexto = (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)
if(ano_bissexto):
    print('O ano {} é um ano BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é um ano BISSEXTO!'.format(ano))