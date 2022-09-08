valor_saque = int(input('Valor do Saque: R$ '))
if(10 <= valor_saque <= 600):
    notas_100 = int(valor_saque/100)
    notas_50 = int((valor_saque - notas_100*100) / 50)
    notas_10 =  int(((valor_saque - notas_100*100) - notas_50*50)/10)
    notas_5 = int((((valor_saque - notas_100*100) - notas_50*50) - notas_10*10) / 5)
    notas_1 = (((valor_saque - notas_100*100) - notas_50*50) - notas_10*10) - notas_5*5 
    print('Notas para sacar R$ {:.2f}:'.format(valor_saque))
    if(notas_100 != 0):
        print('{} nota(s) de R$ 100,00'.format(notas_100))
    if(notas_50 != 0):
        print('{} nota(s) de R$ 50,00'.format(notas_50))
    if(notas_10 != 0):
        print('{} nota(s) de R$ 10,00'.format(notas_10))
    if(notas_5 != 0):
        print('{} nota(s) de R$ 5,00'.format(notas_5))
    if(notas_1 != 0):
        print('{} nota(s) de R$ 1,00'.format(notas_1))
else:
    print('Valor inválido, tente novamente.')