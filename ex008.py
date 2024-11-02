metros = float(input(' Digite a quantidade de metros '))
cm = metros*100
mm = metros*1000
print('{:.0f} metro(s) tem um total de {:.0f} centimetro(s),\n e um total de {:.0f} milimetro(s). '.format(metros, cm, mm))