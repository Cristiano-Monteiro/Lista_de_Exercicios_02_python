tipo_carne = int(input('Tipo de carne - [1] File Duplo; [2] Alcatra; [3] Picanha : '))
quant_carne = int(input('Quantidade(em Kg) de carne: '))
tipo_pagamento = int(input('Pagamento no cartão Tabajara? [1] Sim; [2] Não : '))

if(tipo_carne == 1):
	tipo_carne = 'File Duplo'
	if(quant_carne <= 5):
		preco_total = 4.90 * quant_carne
	else:
		preco_total = 5.80 * quant_carne
elif(tipo_carne == 2):
	tipo_carne = 'Alcatra'
	if(quant_carne <= 5):
		preco_total = 5.90 * quant_carne
	else:
		preco_total = 6.80 * quant_carne
elif(tipo_carne == 3):
	tipo_carne = 'Picanha'
	if(quant_carne <= 5):
		preco_total = 6.90 * quant_carne
	else:
		preco_total = 7.80 * quant_carne

if(tipo_pagamento == 1):
	tipo_pagamento = 'No cartão Tabajara'
	desconto = 0.05 * preco_total
	preco_final = preco_total - desconto
else:
	tipo_pagamento = 'Cartão Normal'
	desconto = 0
	preco_final = preco_total

print('Tipo de carne:', tipo_carne)
print('Quantidade de carne:', quant_carne)
print('Preço Total: R$ %.2f' %preco_total)
print('Tipo de pagamento:', tipo_pagamento)
print('Valor do desconto: R$ %.2f' %desconto)
print('Valor Final a pagar: R$ %.2f' %preco_final)