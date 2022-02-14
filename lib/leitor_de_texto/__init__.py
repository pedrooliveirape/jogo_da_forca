def lerarquivo(conto):
    lista_palavras = list()
    try:
        a = open(conto, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in a:
            texto = linha.split(' ')
            for palavra in texto:
                p = palavra.lower()
                lista_palavras.append(p)
    finally:
        a.close()

    lista_palavras = maior_seis(lista_palavras)
    lista_palavras = palavra_strip(lista_palavras)
    lista_palavras = limpar_caracteres(lista_palavras)
    return lista_palavras


def maior_seis(lista):
    palavras_maior = list()
    for palavra in lista:
        if len(palavra) >= 6:
            palavras_maior.append(palavra)
    return palavras_maior


def palavra_strip(lista):
    palavras_corrigidas = []
    pontuacao = ',.:;!?/"'
    for palavra in lista:
        a = palavra
        for i in range(len(pontuacao)):
            a = a.replace(pontuacao[i], "")
        palavras_corrigidas.append(a)
    return palavras_corrigidas


def limpar_caracteres(lista):
    lista_limpar = lista
    excluir = []

    for c, palavra in enumerate(lista_limpar):
        palavra = palavra.strip()
        for letra in palavra:
            if not letra.isalpha():
                excluir.append(c)

    excluir.sort(reverse=True)
    for numero in excluir:
        del lista_limpar[numero]

    excluir = []

    for c, palavra in enumerate(lista_limpar):
        if 'ª' in palavra:
            excluir.append(c)
        if 'º' in palavra:
            excluir.append(c)

    excluir.sort(reverse=True)
    for numero in excluir:
        del lista_limpar[numero]

    excluir = []

    for c, palavra in enumerate(lista_limpar):
        if '\n' in palavra:
            excluir.append(c)

    excluir.sort(reverse=True)
    for numero in excluir:
        del lista_limpar[numero]

    return lista_limpar
