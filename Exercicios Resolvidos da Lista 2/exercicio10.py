nota1 = float(input('1ª Nota: '))
nota2 = float(input('2ª Nota: '))
nota3 = float(input('3ª Nota: '))
media_notas = (nota1 + nota2 + nota3) / 3
if(media_notas == 10):
    resultado = 'Aprovado com Distinção'
elif(media_notas >= 7):
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'
print('Média: {:.1f} ; Resultado: {}'.format(media_notas, resultado))