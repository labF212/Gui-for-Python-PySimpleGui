#import sqlite3
from random import randint
import PySimpleGUI as sg
import back

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

def front():
    flayout = [ 
        [sg.Text('Bem vindo')],  #linha 1
        [sg.Button('ENTRAR'),sg.Button('SAIR')] #linha 2
        ]
    window = sg.Window('Recursos Humanos',flayout,size=(500,100),element_justification='center')
    button,values = window.read()

    if button == 'ENTRAR':
        window.close()

    if button == 'SAIR' or button == sg.WIN_CLOSED:
        window.exit()

ID = ''
NAME = back.read_task()

layout = [  [sg.Text('Digite o nome do funcionário'),sg.InputText('',key='-NAME-')],
            [sg.Button('Adicionar')],
            [sg.Text('')],
            [sg.Text('Funcionário Registado') ],
            [sg.Listbox(NAME,size=(50,10),key='-BOX-') ],
            [sg.Button('Apagar'), sg.Button('Sair')]]
        

front()




# Create the Window
window = sg.Window('Base de Dados de Funcionários', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    button, values = window.read()
    if button == 'Adicionar': # if user closes window or clicks cancel
        ID = randint(1,9999)
        NAME = values['-NAME-'].capitalize()
    
        if NAME != '':
        #dbase.write(ID,NAME)
            back.write(ID,NAME)

        NAME = back.read_task()

    window.find_element('-NAME-').Update('')
    window.find_element('-BOX-').Update(NAME)

    if button == 'Apagar':
        if NAME:
            x=values['-BOX-'][0]
            back.delete(x)
            NAME = back.read_task()
            window.find_element('-BOX-').Update(NAME)
    
    #if button == 'Sair':
    if button == 'Sair' or button ==  sg.WIN_CLOSED:
        window.close() 
        break

window.close()