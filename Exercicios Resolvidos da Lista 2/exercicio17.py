quantidade_morangos = int(input('Quantidade(em Kg) de morangos: '))
quantidade_macas = int(input('Quantidade(em Kg) de maças: '))

if(quantidade_morangos <= 5):
	preco_morango = 2.50 * quantidade_morangos
else:
	preco_morango = 2.20 * quantidade_morangos

if(quantidade_macas <= 5):
	preco_macas = 1.80 * quantidade_macas
else:
	preco_macas = 1.50 * quantidade_macas

preco_total = preco_morango + preco_macas
quantidade_total = quantidade_morangos + quantidade_macas

print('Quantidade Total:', quantidade_total)
print('Preço SEM desconto: R$ %.2f' %preco_total)

if(quantidade_total > 8 or preco_total > 25):
	desconto = 0.10 * preco_total
	preco_final = preco_total - desconto
	print('Preço COM desconto: R$ %.2f' %preco_final)