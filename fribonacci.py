anterior = 0
proximo = 0
n = int(input('Digite um numero inteiro'))
while(proximo < n):
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior
  if(proximo == 0):
    proximo = proximo + 1