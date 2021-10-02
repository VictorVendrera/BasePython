from random import randint
computador= randint(0, 5)
sair = True
while sair:
    print('-=-'*20)
    print('Vou pensar em número de 0 a 5 tente advinhar...')
    print('-=-'*20)
    n=int(input('Em que número eu pensei?'))
    if n == computador:
        print('Parabens!!Você consegiu me vencer!!')
    else:
        print('Você perdeu!! Eu pensei no número {} não no {}'.format(computador,n))
    x=int( input('Aperte 1 para jogar de novo 0 para encerrar'))
    if x == 1:
        sair= True
    elif x==0:
        sair=False
