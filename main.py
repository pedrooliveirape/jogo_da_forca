from lib.interface import cabecalho
from lib.arquivos import validar_palavra, validar_palpite
from time import sleep


cabecalho('JOGO DA FORCA')
digite_palavra = str(input('Digite uma palavra com mais de 6 letras: ')).upper()
palavra = validar_palavra(digite_palavra)
print(f'a palabra tem {len(palavra)} letras:')

conjunto_palpites = set()
palavra = list(palavra)
lista_resposta = list('_' * len(palavra))
erros = 0
for letra in lista_resposta:
    print(letra, end=' ')
print('\n ')

while palavra != lista_resposta:
    digite_palpite = str(input('Digite uma letra: ')).upper()[0]
    palpite = validar_palpite(conjunto_palpites, digite_palpite)
    conjunto_palpites.add(palpite)

    for c, letra in enumerate(palavra):
        if letra == palpite:
            lista_resposta.insert(c, palpite)
            lista_resposta.pop(c+1)
    if palpite not in palavra:
        print(f'ERRO! A palavra não tem a letra {palpite.upper()}')
        erros += 1
        if erros == 4:
            break

    sleep(0.5)
    print(f'\033[33mErro: {erros}/4\033[m')
    print()
    for letra in lista_resposta:
        print(letra, end=' ')
    print()
    print('Palpites digitados: ', end=' ')
    for letra in conjunto_palpites:
        print(letra, end='-')
    print('\n')

print('FIM')
