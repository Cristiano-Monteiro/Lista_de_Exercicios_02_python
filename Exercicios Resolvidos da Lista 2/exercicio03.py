numero_semana = int(input('Digite um número inteiro entre 1 e 7: '))
if(numero_semana <= 0 or numero_semana > 7):
    print('VALOR INVÁLIDO.')
else:
    if(numero_semana == 1):
        dia_semana = 'DOMINGO'
    elif(numero_semana == 2):
        dia_semana = 'SEGUNDA'
    elif(numero_semana == 3):
        dia_semana = 'TERÇA'
    elif(numero_semana == 4):
        dia_semana = 'QUARTA'
    elif(numero_semana == 5):
        dia_semana = 'QUINTA'
    elif(numero_semana == 6):
        dia_semana = 'SEXTA'
    elif(numero_semana == 7):
        dia_semana = 'SÁBADO'
    print('Dia correspondente da semana: {}'.format(dia_semana))