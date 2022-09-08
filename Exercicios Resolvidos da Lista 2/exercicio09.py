numero = int(input('Digite um número menor que 1000: '))
if(0 < numero < 1000):
    if(numero >= 100):
        centena = int(numero / 100)
        dezena = int(((int(numero / 10) * 10) - (centena * 100))/10)
        unidade = numero - (centena * 100) - (dezena * 10)
        print('{} = {} centena(s), {} dezena(s) e {} unidade(s)'.format(numero, centena, dezena, unidade))
    elif(numero >= 10):
        dezena = int(numero / 10)
        unidade = numero - (dezena * 10)
        print('{} = {} dezena(s) e {} unidade(s)'.format(numero, dezena, unidade))
    else:
        print('{} = {} unidade(s)'.format(numero, numero))
else:
    print('O número é INVÁLIDO')