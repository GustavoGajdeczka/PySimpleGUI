from PySimpleGUI import PySimpleGUI as sg
from controller import make_table
from model import *

sg.theme('DarkGreen')

def menu():
    layout = [
        [sg.Text("== Imobiliaria Gajdeczka ==")],
        [sg.Button('Cadastrar Imovel', key='imovel'), sg.Button('Listar Imoveis', key='lista')],
        [sg.Button('sair')],
    ]
    return sg.Window('Menu', layout, finalize=True)

def cadastra():
    layout = [
        [sg.Text("== Cadastro de Imovel ==")],
        [sg.Text("Endereço: "),sg.Input(key='endereco')],
        [sg.Text("Valor do aluguel: "),sg.Input(key='aluguel')],
        [sg.Text("Andar do apartamento: "),sg.Input(key='andar')],
        [sg.Text("Taxa de condomínio: "),sg.Input(key='taxa')],
        [sg.Button('cadastrar')]
    ]
    return sg.Window('Cadastra Imovel', layout, finalize=True)

def ficha():
    layout = [[sg.Table(values=data, headings=headings, max_col_width=25,
            auto_size_columns=True,
            display_row_numbers=False,
            justification='right',
            num_rows=5,
            alternating_row_color='lightyellow',
            key='-TABLE-',
            row_height=35,
            tooltip='This is a table')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Ficha', layout, finalize=True)