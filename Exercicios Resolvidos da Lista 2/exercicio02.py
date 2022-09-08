valor_hora = float(input('Valor da sua hora: R$ '))
quantidade_horas = int(input('Quantidade de horas trabalhadas no mês: '))
salario_bruto = valor_hora * quantidade_horas
# DESCONTO DO IR:
if(salario_bruto <= 900):
    desconto_ir = 0
elif(salario_bruto <= 1500):
    desconto_ir = 0.05
elif(salario_bruto <= 2500):
    desconto_ir = 0.10
else:
    desconto_ir = 0.20
# DESCONTO INSS:
desconto_inss = 0.10 * salario_bruto
# DEPOSITO DO FGTS:
deposito_fgts = 0.11 * salario_bruto
total_descontos = desconto_inss + (desconto_ir * salario_bruto)
salario_liquido = salario_bruto - total_descontos
print('Salário Bruto: ({} * {}) -> R$ {:.2f}'.format(valor_hora, quantidade_horas, salario_bruto))
print('(-) IR ({:.0f}%)  -> R$ {:.2f}'.format(desconto_ir*100, desconto_ir*salario_bruto))
print('(-) INSS (10%)  -> R$ {:.2f}'.format(desconto_inss))
print('FGTS (11%)  -> R$ {:.2f}'.format(deposito_fgts))
print('Total de Descontos -> R$ {:.2f}'.format(total_descontos))
print('Salário Líquido  -> R$ {:.2f}'.format(salario_liquido))