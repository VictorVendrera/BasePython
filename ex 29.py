vel= int(input('Qual é a velocidade atual do carro?'))
if vel > 80:
    print('\33[0;31mMultado! você excedeu o limite de 80 km/h\33[m')
    multa = (vel-80)
    print('\33[0;31mVocê deve pagar uma multa de {}R$\33[m'.format(multa))
print('\33[0;34mTenha um Bom Dia! Dirija com segurança\33[m')