salario_colaborador = float(input('Digite seu salário: R$ '))
if(salario_colaborador > 1500):
    reajuste = 0.05
elif(700 < salario_colaborador <= 1500):
    reajuste = 0.10
elif(280 < salario_colaborador <= 700):
    reajuste = 0.15
else:
    reajuste = 0.20
aumento_salario = reajuste * salario_colaborador
novo_salario = salario_colaborador + aumento_salario
print('Salário antes do Reajuste: R$ {:.2f}'.format(salario_colaborador))
print('Percentual de aumento aplicado: {:.0f}%'.format(reajuste * 100))
print('Valor do aumento: R$ %.2f' %aumento_salario)
print('Novo Salário após o aumento: R$ %.2f' %novo_salario)