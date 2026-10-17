from lojinha.lib.cores import *
from time import sleep

def linha(tam=43):
    return '-' * tam

def titulo(msg):
    print(linha())
    print(f'{background["verde"]}{CORES["preto"]}{msg.center(43)}{CORES["limpa"]}')
    print(linha())
    sleep(1)

def menu(lst):
    titulo('SISTEMA DE ESTOQUE DE PRODUTOS')
    c = 1
    for opcao in lst:
        if c == 3:
            print(f'{CORES["vermelho"]}{c} - {CORES["limpa"]}{CORES["ciano"]}{opcao}{CORES["limpa"]}')
        else:
            print(f'{CORES["amarelo"]}{c} - {CORES["limpa"]}{CORES["ciano"]}{opcao}{CORES["limpa"]}')
        c += 1
    sleep(0.5)
    print(linha())
    opc = leiaInt(f'{CORES["azul"]}Digite a sua opção: {CORES["limpa"]}')
    sleep(0.5)
    return opc

def leiaInt(opc):
    while True:
        try:
            n = int(input(opc))
        except (ValueError, TypeError):
            print(f'{CORES["vermelho"]}Valor inválido, digite um número: {CORES["limpa"]}')
        except KeyboardInterrupt:
            print(f'\n{CORES["amarelo"]}O usuário interrompeu a ação.{CORES["limpa"]}')
            sleep(0.5)
            return 3
        else:
            return n