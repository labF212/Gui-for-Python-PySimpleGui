import PySimpleGUI as sg
import time

layout = [
    [sg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20), key='-PBAR-', bar_color=('green', 'blue'), border_width=2)],
    [sg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 16), justification='center', expand_x=True)],
    [sg.Button('Test')]
]

window = sg.Window('Progress Bar', layout, size=(715, 150))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Test':
        window['-PBAR-'].update(max=0, bar_color=('green', 'blue'))
        window['Test'].update(disabled=True)
        for i in range(100):
            window['-PBAR-'].update(current_count=i + 1)
            window['-OUT-'].update(str(i + 1))
            time.sleep(0.01)
            if i + 1 >= 75:
                window['-PBAR-'].update(bar_color=('red', 'blue'))
            elif i + 1 >= 50:
                window['-PBAR-'].update(bar_color=('yellow', 'blue'))
        window['Test'].update(disabled=False)   

window.close()
