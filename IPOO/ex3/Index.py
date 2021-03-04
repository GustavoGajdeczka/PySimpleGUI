from PySimpleGUI import PySimpleGUI as sg
from escola import aluno
import ast

# Janelas e Layout
sg.theme("darkgreen")

def menu():
    layout = [
        [sg.Text("== Escola ==")],
        [sg.Button('Cadastra Aluno', key='aluno'), sg.Button('Adiciona Notas', key='nota')],
        [sg.Button('Ficha do aluno', key='ficha')],
        [sg.Button('sair')],
    ]
    return sg.Window('Menu', layout, finalize=True)
def cadastra():
    layout = [
        [sg.Text("== Cadastro de Aluno ==")],
        [sg.Text("Nome: "),sg.Input(key='nome')],
        [sg.Text("Endereço: "),sg.Input(key='endereco')],
        [sg.Button('cadastrar')]
    ]
    return sg.Window('Cadastra aluno', layout, finalize=True)
def nota():
    layout = [
        [sg.Text("== Cadastras Notas ==")],
        [sg.Text("Nota 1° Bimestre"), sg.Input(key='nota1')],
        [sg.Text("Nota 2° Bimestre"), sg.Input(key='nota2')],
        [sg.Text("Nota 3° Bimestre"), sg.Input(key='nota3')],
        [sg.Text("Nota 4° Bimestre"), sg.Input(key='nota4')],
        [sg.Button('Salva')]
    ]
    return sg.Window('Cadastra Notas', layout, finalize=True)
def ficha(nome, endereco, media):
    layout = [
        [sg.Text("== Ficha do Aluno ==")],
        [sg.Text('Nome: '), sg.Text(nome)],
        [sg.Text('Endereço: '), sg.Text(endereco)],
        [sg.Text('Media: '), sg.Text(media)],
    ]
    return sg.Window('Ficha do Aluno', layout, finalize=True)

# Janelas Iniciais 
janela_menu, janela_cadastra, janela_nota, janela_ficha = menu(), None, None, None

# Logica
Aluno = aluno()
while True:
    window, event, values = sg.read_all_windows()
    if window == janela_menu and event == sg.WIN_CLOSED:
        break

    if window == janela_menu and event =='aluno':
        janela_cadastra = cadastra()
        janela_menu.hide()
    if window == janela_cadastra and event == 'cadastrar':
        if not values['nome'] and not values['endereco']:
            sg.popup('ERRO: campo vazio', title = 'ERRO')
        else:
            Aluno.cadastra(values['nome'], values['endereco'])
            janela_cadastra.hide()
            janela_menu.un_hide()
    if window == janela_menu and event == 'nota':
        if Aluno.verifica() == (True, False) or Aluno.verifica() == (True, True):
            janela_nota = nota()
            janela_menu.hide()
        else:
            sg.popup("ERRO: Aluno Não Cadastrado", title = "ERRO")
    if window == janela_nota and event == 'Salva':
        if not values['nota1'] and not values['nota2'] and not values['nota3'] and not values['nota4']:
            sg.popup('ERRO: campo vazio', title = 'ERRO')
        else:
            nota = ast.literal_eval(values['nota1'])
            Aluno.setNota(nota)
            nota = ast.literal_eval(values['nota2'])
            Aluno.setNota(nota)
            nota = ast.literal_eval(values['nota3'])
            Aluno.setNota(nota)
            nota = ast.literal_eval(values['nota4'])
            Aluno.setNota(nota)
            Aluno.media()
            janela_nota.hide()
            janela_menu.un_hide()
    if window == janela_menu and event == 'ficha':
        if Aluno.verifica() == (True, True):
            janela_menu.hide()
            nome, endereco, media = Aluno.imprimeDados()
            janela_ficha = ficha(nome, endereco, media)
        else:
            sg.popup("ERRO: Aluno ou Nota Não Cadastrado", title = "ERRO")
    if event == sg.WIN_CLOSED or event == 'sair':
        break
window.close()