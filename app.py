import os

restaurantes = [{'nome':'Mc Donalds' , 'categoria':'Fast-food', 'ativo':False},
                {'nome':'Pizza Hut', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Levíssimo', 'categoria':'Salada', 'ativo':False}]

def exibir_logo():
    print("__________ 🇮​​​​​🇫​​​​​🇴​​​​​🇴​​​​​🇩 __________​​​​​\n")

def exibir_menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair \n")

def encerrar_aplicacao():
    os.system('clear')
    print("Encerrando aplicação...")

def voltar_ao_menu_inicial():
    input('\nAperte qualquer tecla para retornar ao menu inicial: ')
    main()

def opcao_invalida():
    print('A opção que você escolheu é inválida \n')

def exibir_subtitulo(texto):
    os.system('clear')
    print(f'{texto}\n')

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurante_novo = {'nome':nome_do_restaurante , 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(restaurante_novo)
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!')
    
    voltar_ao_menu_inicial()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes...')
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'
        print(f'- {nome_do_restaurante} | {categoria} | {ativo}')
    
    voltar_ao_menu_inicial()

def alterar_estado_restaurante():
    exibir_subtitulo('Alteração de estado de restaurante')
    restaurante_selecionado = input('Digite o nome do restaurante que deseja alterar estado: ')
    encontrou_restaurante = False

    for restaurante in restaurantes:
        if restaurante_selecionado == restaurante['nome']:
            encontrou_restaurante = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante_selecionado} foi ATIVADO com sucesso!' if restaurante['ativo'] else f'O restaurante {restaurante_selecionado} foi DESATIVADO com sucesso!'
            print(mensagem)
    if not encontrou_restaurante:
        print('Restaurante não cadastrado.')

    voltar_ao_menu_inicial()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção acima: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alterar_estado_restaurante()

        elif opcao_escolhida == 4 :
            encerrar_aplicacao()

        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_logo()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
    