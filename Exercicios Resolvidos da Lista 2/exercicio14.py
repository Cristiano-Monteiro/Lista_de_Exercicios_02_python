numero1 = float(input('1º Número: '))
numero2 = float(input('2º Número: '))
operacao = str(input('Qual operação deseja realizar? [+,-,*,/]: '))
operacoes_validas = operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/'
if(operacoes_validas):
    if(operacao == '+'):
        resultado = numero1 + numero2
    elif(operacao == '-'):
        resultado = numero1 - numero2
    elif(operacao == '*'):
        resultado = numero1 * numero2
    elif(operacao == '/'):
        resultado = numero1 / numero2

    par_ou_impar = 'PAR'
    if(resultado % 2 != 0):
        par_ou_impar = 'ÍMPAR'
    positivo_ou_negativo = 'POSITIVO'
    if(resultado < 0):
        positivo_ou_negativo = 'NEGATIVO'
    inteiro_ou_decimal = 'INTEIRO'
    if(resultado % 1 != 0):
        inteiro_ou_decimal = 'DECIMAL'

    print('==> {} {} {} = {}'.format(numero1, operacao, numero2, resultado))
    print('O resultado {} é um número '.format(resultado), end='')
    print('{}, {} e {}'.format(par_ou_impar, positivo_ou_negativo, inteiro_ou_decimal))
else:
    print('Operação Inválida! Tente novamente.')