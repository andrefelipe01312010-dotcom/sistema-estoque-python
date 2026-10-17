from lojinha.lib.interface import titulo
from lojinha.lib.cores import *
from time import sleep

def arquivoExiste(nome):
    try:
        with open(nome, 'r') as a:
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        with open(nome, 'w+') as a:
            pass
    except Exception as erro:
        print(f'{CORES["vermelho"]}Ocorreu um erro na criação do arquivo. Causa: {erro}{CORES["limpa"]}')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(nome):
    try:
        with open(nome, 'r') as a:
            titulo('PRODUTOS CADASTRADOS')
            print(f'{"PRODUTO":<15}{"PREÇO":>10}{"QUANT":>10}')
            for linha in a:
                dado = linha.split(';')
                dado[2] = dado[2].replace('\n', '')
                preco_formatado = f'R${float(dado[1]):.2f}'
                print(f'{dado[0]:<15}{preco_formatado:>10}{dado[2]:>10}')
    except Exception as erro:
        print(f'{CORES["vermelho"]}Ocorreu um erro na leitura do arquivo. Causa: {erro}{CORES["limpa"]}')
    sleep(1.5)


def cadastrar(arq, nome, preco, quant):
    try:
        with open(arq, 'a') as a:
            a.write(f'{nome};{preco:.2f};{quant}\n')
            sleep(1)
            print(f'{CORES["verde"]}{nome} adicionado(a).{CORES["limpa"]}')
            sleep(1)
    except:
        print('Ocorreu um erro ao adicionar o produto.')