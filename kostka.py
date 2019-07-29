def kostka(znak, wysokosc, szerokosc):
  if len(znak) != 1:
    raise Exception('musi być znak (znak = 1)')
  if wysokosc <= 2:
    raise Exception('wysokosc musi byc > 2')
  if szerokosc <= 2:
    raise Exception('szerokosc musi być > 2')
  print(znak * szerokosc)
  for i in range(wysokosc - 2):
    print(znak + (' ' * (szerokosc -2)) + znak)
  print(znak * szerokosc)

for z, w, s in (('*', 6, 6), ('0', 10, 5,), ('x', 1, 3),('ZZ', 3, 3)):
  try:
    kostka(z, w, s)
  except Exception as blad:
    print('wyjątek: ' + str(blad))
