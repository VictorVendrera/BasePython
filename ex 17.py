import math
co=float(input('Digite a medida do cateto oposto'))
ca=float(input('Digite a medida do cateto adjascente'))
hi=math.hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))

#Maneira tradicional
#co=float(input('Digite a medida do cateto oposto'))
#ca=float(input('Digite a medida do cateto adjascente'))
#hi= (co ** 2 + ca ** 2)**(1/2)
#print('O valor da hipotenusa é {:.2f}'.format(hi))
