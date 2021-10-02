#Usando apenas o trunc
from math import trunc
num=float(input("Digite um numero"))
print('O valor digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))

##Usando a biblioteca math inteira
# import math
#num=float(input("Digite um numero"))
#print('O valor digitado foi {} e sua parte inteira é {}'.format(num, math.trunc(num)))

#Outra maneira sem usar a biblioteca
num=float(input("Digite um numero"))
print('O valor digitado foi {} e sua parte inteira é {}'.format(num, int(num)))
