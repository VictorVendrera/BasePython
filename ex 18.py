from math import sin, cos, tan, radians
angulo= float(input('Digite a medida do angulo'))
seno= sin(radians(angulo))
print('O angulo {} tem o seno de {:.2f}'.format(angulo, seno))
coseno= cos(radians(angulo))
print('O angulo {} tem o coseno de {:.2f}'.format(angulo, coseno))
tangente= tan(radians(angulo))
print('O angulo {} tem o tangente de {:.2f}'.format(angulo, tangente))