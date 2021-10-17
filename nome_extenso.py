n = int(input('Digite um número: '))

numeros_unidade = {
    0: 'zero',
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
}

numeros_dezena = {
    2: 'vinte',
    3: 'trinta',
    4: 'quarenta',
    5: 'cinquenta',
    6: 'sessenta',
    7: 'setenta',
    8: 'oitenta',
    9: 'noventa'
}

numeros_dez = {
    0: 'dez',
    1: 'onze',
    2: 'doze',
    3: 'treze',
    4: 'catorze',
    5: 'quinze',
    6: 'dezesseis',
    7: 'dezessete',
    8: 'dezoito',
    9: 'dezenove'
}

numeros_centena = {
    1: 'cento',
    2: 'duzentos',
    3: 'trezentos',
    4: 'quatrocentos',
    5: 'quinhentos',
    6: 'seiscentos',
    7: 'setecentos',
    8: 'oitocentos',
    9: 'novecentos'
}


def dezena_final_zero(n):
    if 10 <= n < 20:
        return f'{numeros_dez[u]}'
    if 20 <= n < 100:
        return f'{numeros_dezena[d]}'


def dezena(n):
    if u == 0:
        return dezena_final_zero(n)
    elif 10 <= n <= 19:
        return f'{numeros_dez[u]}'
    else:
        return f'{numeros_dezena[d]} e {numeros_unidade[u]}'


def centena(n):
    aux = n%100
    if c==1 and d==0 and u==0:
        return f'cem'
    elif d==0 and u==0:
        return f'{numeros_centena[c]}'
    elif d==0:
        return f'{numeros_centena[c]} e {numeros_unidade[u]}'
    else:
        return f'{numeros_centena[c]} e {dezena(aux)}'

if __name__ == '__main__':
    u = n % 10
    d = (n//10) % 10
    c = n//100

    if n >= 0 and n < 10:
        print(f'{numeros_unidade[u]}')
    if n >= 10 and n <= 99:
        print(dezena(n))
    if n > 99 and n <= 999:
        print(centena(n))
