from lib.interface import cabecalho, linha
from lib.arquivos import validar_palavra, validar_palpite, sortea_palavra
from lib.leitor_de_texto import lerarquivo
from time import sleep


cabecalho('JOGO DA FORCA')
endereco_texto = 'lib/leitor_de_texto/contos/joao_e_maria.txt'
receber_palavras = lerarquivo(endereco_texto)
palavra_sorteada = sortea_palavra(receber_palavras).upper()
palavra = validar_palavra(palavra_sorteada)
print(f'A palavra tem {len(palavra)} letras:')

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

    sleep(0.5)
    print(f'\033[33mErro: {erros}/4\033[m')
    for letra in lista_resposta:
        print(letra, end=' ')
    print()
    print('Palpites digitados: ', end=' ')
    for letra in conjunto_palpites:
        print(letra, end='-')

    print(f'\n{linha()}')

    if erros == 4:
            break

print('FIM')
