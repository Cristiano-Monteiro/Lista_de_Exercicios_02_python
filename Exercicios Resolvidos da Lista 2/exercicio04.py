nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))
media_notas = (nota1 + nota2) / 2
# ATRIBUIÇÃO DE CONCEITOS:
if(media_notas > 9 and media_notas <= 10):
    conceito = 'A'
elif(media_notas > 7.5 and media_notas <= 9):
    conceito = 'B'
elif(media_notas > 6 and media_notas <= 7.5):
    conceito = 'C'
elif(media_notas > 4 and media_notas <= 6):
    conceito = 'D'
elif(media_notas >= 0 and media_notas <= 4):
    conceito = 'E'
# RESULTADOS:
print('Notas: {} e {}'.format(nota1, nota2))
print('Média das notas: {:.2f}'.format(media_notas))
print('Conceito: {}'.format(conceito))
if(conceito == 'A' or conceito == 'B' or conceito == 'C'):
    print('Resultado: APROVADO')
else:
    print('Resultado: REPROVADO')