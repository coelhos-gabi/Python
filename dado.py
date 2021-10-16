import random


def sorteio():
    return random.randint(1, 6)


def erro(entrada):
    while entrada != 's' and entrada != 'sim' and entrada != 'n' and entrada != 'nao':
        print('Opa! Tente de novo')
        entrada = input('Quer jogar o dado?')
        entrada=entrada.lower()
    main(entrada)


def main(entrada):
    while entrada == 's' or entrada == 'sim':
        print(sorteio())
        entrada = input('Deseja jogar de novo?')
        entrada = entrada.lower()

    if entrada == 'n' or entrada == 'nao':
        print(f'Fim de jogo!')

    else:
        erro(entrada)

if __name__ == '__main__':
    print('Bem vindo ao jogo do dado!')
    nome = input('Digite seu nome: ')
    print(f'Olá, {nome.capitalize()}')
    print('Quer jogar o dado?')
    entrada = input('Digite s para sim ou n para não ')
    entrada = entrada.lower()
    main(entrada)