numero_usuario = float(input('Digite um número: '))
if(numero_usuario % 1 == 0):
    print('O número {:.0f} é INTEIRO'.format(numero_usuario))
else:
    print('O número {} é DECIMAL'.format(numero_usuario))