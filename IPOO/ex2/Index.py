from PySimpleGUI import PySimpleGUI as sg
from triangulo import Triangulo
import ast

sg.theme("darkgreen")

layout = [
    [sg.Text("Triangulo")],
    [sg.Text("Base: "), sg.Input(key='base', size = '9')],
    [sg.Text("Altura: "), sg.Input(key='altura', size = '9')],
    [sg.Button('Calcula'), sg.Button('sair')]
]

window = sg.Window('Area do Triangulo', layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'sair' :
        break
    if event == 'Calcula':
        base = ast.literal_eval(value['base'])
        altura = ast.literal_eval(value['altura'])
        tri = Triangulo(base, altura)
        calc = tri.area()
        sg.popup("A área do triângulo (base * altura) / 2 = " + str(calc), title = "Triangulo")
window.close()