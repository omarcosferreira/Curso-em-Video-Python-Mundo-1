distancia = float(input('Qual a distancia da viagem ?'))
if distancia < 200:
    print("""para viajar {:.2f}km;
    o preço da sua passagem fica R$0,50 por km,
    que resultam em R${:.2f}""".format(distancia, (distancia *0.50)))
else:
    print("""para viajar {:.2f}km;
    o preço da sua passagem fica R$0,45 por km,
    que resultam em R${:.2f}""".format(distancia,(distancia *0.45)))
print('_-_' *20)
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('voce vai viajar {:.2f}km\ne o preço da sua passagem fica R${:.2f}'.format(distancia, preco))
