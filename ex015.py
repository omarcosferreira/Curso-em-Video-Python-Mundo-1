km = float(input('Qual a quantidade de km percorridos? '))
diaria = int(input('E quantos dias durou a sua viagem? '))
custo_diaria = diaria * 60
custo_km = km * 0.15
print('Você andou {:.0f}km durante a sua viagem de {} dias. isso irá te custar um total de R${:.2f}, resultado entre a soma de R${:.2f} pelos km percorridos e R${:.2f} pela diaria do carro.'.format(km, diaria,custo_diaria + custo_km, custo_km, custo_diaria))
