from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text("Digite o seu Nome")],
    [sg.Text("Nome: "), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
]
# Janela
window = sg.Window('Hello World', layout)
# Eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' :
        break
    print("Você digitou", values[0])

window.close()
