from PySimpleGUI import PySimpleGUI as sg
from model import Apartamento
from view import *


sg.theme('DarkGreen')

janela_menu, janela_cadastra, janela_ficha = menu(), None, None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela_menu and event == sg.WIN_CLOSED:
        break

    if window == janela_menu and event == 'imovel':
        janela_cadastra = cadastra()
        janela_menu.hide()
    if window == janela_cadastra and event == 'cadastrar':
        if not values['endereco'] and not values['aluguel']:
            sg.popup('ERRO: campo vazio', title = 'ERRO')
        else:
            janela_cadastra.hide()
            janela_menu.un_hide()
    if window == janela_menu and event == 'lista':
        janela_menu.hide()
        janela_ficha = ficha()
    if window == janela_ficha and event == 'Voltar':
        janela_ficha.hide()
        janela_menu.un_hide()
    if event == 'sair':
        break

window.close()