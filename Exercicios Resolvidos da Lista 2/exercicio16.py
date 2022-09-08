quantidade_litros = int(input('Quantidade de Litros: '))
tipo_combustivel = str(input('Tipo de combustível [A - álcool; G - gasolina]: '))

if(tipo_combustivel == 'A' or tipo_combustivel == 'G'):
    if(tipo_combustivel == 'A'):
        preco_litro = quantidade_litros * 1.90
        if(quantidade_litros <= 20):
            desconto = 0.03 * preco_litro
        else:
            desconto = 0.05 * preco_litro
    elif(tipo_combustivel == 'G'):
        preco_litro = quantidade_litros * 2.50
        if(quantidade_litros <= 20):
            desconto = 0.04 * preco_litro
        else:
            desconto = 0.06 * preco_litro
    preco_total = preco_litro - desconto
    print('Tipo de combustível:',tipo_combustivel)
    print('Número de litros:',quantidade_litros)
    print('Desconto: R$ %.2f' %desconto)
    print('Preço sem desconto: R$ %.2f' %preco_litro)
    print('Preço com desconto: R$ %.2f' %preco_total)
else:
    print('Tipo de combustível não identificado! Tente novamente.')