valorA = int(input('Digite o valor A: '))
if(valorA != 0):
    valorB = int(input('Digite o valor B: '))
    valorC = int(input('Digite o valor C: '))
    delta = valorB**2 - 4*valorA*valorC
    if(delta < 0):
        print('A equação NÃO possui raizes reais')
    elif(delta == 0):
        raiz = (valorB*(-1)) / 2*valorA
        print('A equação possui apenas uma raiz real: x = {}'.format(raiz))
    else:
        raiz1 = (valorB*(-1) + delta**(1/2)) / 2*valorA
        raiz2 = (valorB*(-1) - delta**(1/2)) / 2*valorA
        print('A equação possui duas raizes reais: x1 = {} e x2 = {}'.format(raiz1, raiz2))
else:
    print('A equação NÃO é do 2º Grau, pois o valor A = 0')