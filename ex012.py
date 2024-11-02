preco = float(input(' Digite o preço de um produto: '))
  # Calcula 5% do preço
  #desconto = preco * 5/100
  #novo_preco = preco - (preco * 5/100)
desconto = 0.95 * preco
print(' O preço deste produto é R${:.2f}, e com o desconto de 5% ele fica por R${:.2f}'.format(preco, desconto))
