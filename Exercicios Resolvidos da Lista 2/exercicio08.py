dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

dia_valido = 1 <= dia <= 31
mes_valido = 1 <= mes <= 12
ano_valido = 1900 <= ano <= 2500
ano_bissexto = (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)
data_valida = True

if(dia_valido):
    if(mes_valido):
        if(mes == 4 or mes == 6 or mes == 9 or mes == 11):
            if((1 <= dia <= 30) == False):
                data_valida = False
        else:
            if(mes == 2):
                if(ano_bissexto):
                    if((1 <= dia <= 29) == False):
                        data_valida = False
                else:
                    if((1 <= dia <= 28) == False):
                        data_valida = False
    else:
        data_valida = False
else:
    data_valida = False

if(ano_valido == False):
    data_valida = False

if(data_valida):
    print('A data {}/{}/{} é válida'.format(dia,mes,ano))
else:
    print('A data {}/{}/{} NÃO é válida'.format(dia,mes,ano))