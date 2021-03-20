from pytube import YouTube
import PySimpleGUI as sg 
import os

sg.theme('DarkGreen')

dir_path = str(os.path.dirname(os.path.realpath(__file__)) + '\path')


layout = [
    [sg.Text('PyTube')],
    [sg.Text('Pasta destino', size=(15, 1)), sg.Input(dir_path, key= 'path', size=(30, 1)), sg.FolderBrowse(target='path')],
    [sg.Text('URL', size=(15, 1)), sg.Input(key= 'url', size=(30, 1))],
    [sg.Text('Resolução', size=(15, 1)), sg.Combo(values=['Video', 'Musica'], key='res', size=(10,1))],
    [sg.Button('Fechar', key='Close'), sg.Button('Baixar', key='baixar')]
]

window = sg.Window('PyTube', layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Close':
        break

    if event == 'baixar':
        yt = YouTube(values['url'])
        if values['res'] == 'Video':
            ys = yt.streams.get_highest_resolution()
        else:
            musica = yt.streams.filter(only_audio=True).all()
            ys = musica[0]

        try:
            print("Baixando...")
            ys.download(values['path'])
            print("!Download Finalizado")
            sg.Popup('Download Finalizado')
        except ValueError:
            print("ERRO:")

window.close()
