from PySimpleGUI import PySimpleGUI as sg
from circulo import circulo
import ast


# Layout
sg.theme('DarkGreen')
layout = [
    [sg.Text("Area do Circulo")],
    [sg.Text("Raio: "), sg.Input(key = '-IN-', enable_events=True, size="5")],
    [sg.Button('calcular'), sg.Button('sair')]
]
# Janela
window = sg.Window('Area do Circulo', layout)
# Eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'sair' :
        break
    if event == '-IN-' and values['-IN-']:
        try:
            in_as_float = float(values['-IN-'])
        except:
            if len(values['-IN-']) == 1 and values['-IN-'][0] == '-':
                continue
            window['-IN-'].update(values['-IN-'][:-1])
    if event == 'calcular':
        print(values['-IN-'])
        area = ast.literal_eval(values['-IN-'])
        Circ = circulo(area)
        area = Circ.area()
        sg.popup("A área do círculo (π * Raio²): " + str(area), title = "calc")

window.close()
