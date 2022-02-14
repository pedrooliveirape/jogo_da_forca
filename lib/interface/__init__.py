def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt, lin=42):
    print(linha(lin))
    print(txt.center(lin))
    print(linha(lin))


def menu(lista, lin=42):
    cabecalho('MENU PRINCIPAL', lin)
    for c, item in enumerate(lista):
        print(f'\033[33m{c + 1}\033[m - \033[34m{item}\033[m')
    print(linha(lin))
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc

