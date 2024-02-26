import os

restaurantes = [
    {'nome': 'JP Pizzaria', 'categoria': 'Pizzaria', 'ativo': False}, 
    {'nome': 'Bea Sushi', 'categoria': 'Japonesa', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
    ]

def exibir_nome_do_programa():
    print('''
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    ''')

def exibir_opcoes():
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)
    print()

def finalizar_app():
    exibir_subtitulo('Encerrando o programa')

def voltar_ao_menu():
    input('\nPressione ENTER para voltar para o menu principal.')
    main()

def opicao_invalida():
    print('Opção inválida')
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f'  {"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    voltar_ao_menu()

def alterar_estado_do_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')
    voltar_ao_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opicao_invalida()
    except:
        opicao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()