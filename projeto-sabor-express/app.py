import os

restaurantes = [{'nome':'Azulporã', 'categoria':'Hambúrgueria', 'ativo':False}, {'nome':'Rubrus', 'categoria':'Bar e Restaurante', 'ativo':True}]

def exibir_nome_do_programa():
    print('𝕾𝖆𝖇𝖔𝖗 𝕰𝖝𝖕𝖗𝖊𝖘𝖘\n')

def exibir_opcoes():
    print('1_ Cadastrar restaurante')
    print('2_ Listar restaurantes')
    print('3_ Alternar estado do restaurante')
    print('4_ Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...')

def voltar_ao_menu_principal():
    input('\nAperte enter para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes:')

    print(f'{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | {'Estado'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterne o estado do seu restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar:')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi destivado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante que você procura não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int (input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__ == '__main__':
    main()
