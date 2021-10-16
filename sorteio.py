# Gerar valor aleatório e o guarda.
# Pergunta repetidas vezes para o usuário chutar o valor até acertar
import random


def tentativa():
    chute = int(input('Tente um número: '))
    if chute > n:
        chute_alto()
    elif chute < n:
        chute_baixo()
    else:
        print(f'Número sorteado: {n} Parabéns! Você acertou!')

def chute_alto():
    print('Chutou alto')
    tentativa()

def chute_baixo():
    print('Chutou baixo')
    tentativa()    

if __name__ == '__main__':
    n = random.randint(0, 20)
    print('Irei sortear um número de 0 a 20, tente descobrir qual')
    try:
        tentativa()
    except TypeError:
        print('Somente números são aceitos')
        tentativa()
    except ValueError:
        print('Somente números são aceitos')
        tentativa()
