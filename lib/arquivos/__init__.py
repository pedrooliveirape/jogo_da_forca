from random import randint


def validar_palavra(msg):
    palavra = msg
    letras = set(palavra)
    while True:
        if len(palavra) >= 6 and len(letras) >= 5:
            return palavra
        else:
            palavra = str(input('Palavra inválida! Digite uma palavra com mais de 6 letras: ')).lower()
            letras = set(palavra)


def validar_palpite(palpites, letra):
    conjunto_palpites = set(palpites)
    letra_palpite = letra
    while True:
        if letra_palpite not in conjunto_palpites:
            return letra_palpite
        else:
            letra_palpite = str(input(f'A letra {letra_palpite.upper()} já foi digitada! Digite outra letra: ')).lower()[0]


def sortea_palavra(lista):
    numero_sorteado = randint(0, len(lista))
    palavra_sorteada = lista[numero_sorteado]
    return palavra_sorteada
