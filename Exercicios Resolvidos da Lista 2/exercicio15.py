pergunta1 = str(input('Telefonou para a vítima? [S/N] '))
pergunta2 = str(input('Esteve no local do crime? [S/N] '))
pergunta3 = str(input('Mora perto da vítima? [S/N] '))
pergunta4 = str(input('Devia para a vítima? [S/N] '))
pergunta5 = str(input('Já trabalhou com a vítima? [S/N] '))

classificacao = 0
if(pergunta1.upper() == 'S'):
    classificacao +=1
if(pergunta2.upper() == 'S'):
    classificacao +=1
if(pergunta3.upper() == 'S'):
    classificacao +=1
if(pergunta4.upper() == 'S'):
    classificacao +=1
if(pergunta5.upper() == 'S'):
    classificacao +=1

if(classificacao == 5):
    print('Classificação: Assassino')
elif(classificacao == 3 or classificacao == 4):
    print('Classificação: Cúmplice')
elif(classificacao == 2):
    print('Classificação: Suspeita')
else:
    print('Classificação: Inocente')