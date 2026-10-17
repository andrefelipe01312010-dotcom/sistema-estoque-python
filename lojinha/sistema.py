from lojinha.lib.interface import *
from lojinha.lib.cores import *
from lojinha.lib.arquivo import *
from time import sleep


arq = 'estoque.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Mostrar todos os produtos cadastrados', 'Cadastrar um novo produto', 'Sair do programa'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        titulo('NOVO CADASTRO')
        while True:
            nome = str(input('Nome: ')).strip()
            if nome == '':
                print(f'{CORES["vermelho"]}ERRO: O nome não pode estar vazio.{CORES["limpa"]}')
            else:
                break

        while True:
            try:
                entrada = input('Preço: ').strip().replace(',', '.')
                if entrada == '':
                    preco = 0
                    break
                else:
                    preco = float(entrada)
                    if preco < 0:
                        print(f'{CORES["vermelho"]}ERRO! O preço não pode ser negativo.{CORES["limpa"]}')
                        continue
                    break
            except ValueError:
                print(f'{CORES["vermelho"]}ERRO: Digite um preço válido.{CORES["limpa"]}')
            except KeyboardInterrupt:
                print(f'\n{CORES["amarelo"]}O usuário interrompeu a ação.{CORES["limpa"]}')

        quant = 0
        while True:
            try:
                quant = int(input('Quantidade: '))
                if quant <= 0:
                    print(f'{CORES["vermelho"]}ERRO: O produto precisa de ao menos 1 unidade.{CORES["limpa"]}')
                else:
                    break
            except ValueError:
                print(f'{CORES["vermelho"]}ERRO: Digite um número válido para a quantidade.{CORES["limpa"]}')
            except KeyboardInterrupt:
                print(f'\n{CORES["amarelo"]}O usuário interrompeu a ação.{CORES["limpa"]}')

        cadastrar(arq, nome, preco, quant)

    elif resp == 3:
        print(f'{CORES["vermelho"]}Finalizando...{CORES["limpa"]}')
        sleep(1)
        break
    else:
        print(f'{CORES["vermelho"]}ERRO! Digite uma opção válida no menu.{CORES["limpa"]}')

titulo('VOLTE SEMPRE!'.center(43))