num = int(input('Digite um numero inteiro'))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m= num//1000 % 10

print('Analisando o número {}...'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))



#print('Unidade {}'.format(n[3]))
#print('Dezena {}'.format(n[2]))
#print('Centena {}'.format(n[1]))
#print('Milhar {}'.format(n[0]))