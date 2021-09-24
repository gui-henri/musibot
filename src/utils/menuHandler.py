import utils.musibotUtils as utils

main_menu_opts = {
    '1': 'Pausar',
    '2': 'Reiniciar música',
    '3': 'Pular música atual',
    '4': 'Adicionar música a lista de reprodução',
    '5': 'Ou Q para sair'
}

pause_opts = {
    '1': 'Continuar',
    '2': 'Reiniciar música',
    '3': 'Pular música atual',
}

def show_main_menu(musibot):
    print('Tocando agora: ' + musibot.play_list_data['playlist'][0])
    print('Escolha um comando: ')
    for key in main_menu_opts.keys():
        print(key, ':', main_menu_opts[key])

def show_pause_menu(musibot):
    print(musibot.play_list_data['playlist'][0] + ' está pausada. O que fazer a seguir?')
    for key in pause_opts.keys():
        print(key, ':', pause_opts[key])


def main_menu(musibot):
    while musibot.is_playing():
        show_main_menu(musibot)

        main_command = input('Comando: ')

        if main_command == '1':
            utils.clear_terminal()
            musibot.pause()
            show_pause_menu(musibot)
            pause_command = input('Comando: ')

            if pause_command == '1':
                utils.clear_terminal()
                musibot.unpause()

            if pause_command == '2':
                utils.clear_terminal()
                musibot.restart()

            if pause_command == '3':
                musibot.stop()
                break

        if main_command == '2':
            utils.clear_terminal()
            musibot.restart()
                
        if main_command == '3':
            musibot.stop()
            break

        if main_command == '4':
            utils.clear_terminal()
            new_mus = input('Digite o nome da música a ser adicionada: ')
            musibot.add_to_playlist(new_mus)
                
        if main_command == 'q' or main_command == 'Q':
            musibot.running = False
            break