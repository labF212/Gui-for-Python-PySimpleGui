#Academia Python
#https://www.youtube.com/watch?v=fgqEPSQhM4Y&list=PLldtDp_gjtrfwk6zmXBIEy-FY_7qqHdfQ
#import sqlite3
from random import randint
#from re import TEMPLATE
import PySimpleGUI as sg
import back_gui

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
TIMES = back_gui.read_task()

layout = [  [sg.Text('Digite a hora             '),sg.InputText('',key='-TIMES-')],
            [sg.Text('Digite a temperatura    '),sg.InputText('',key='-TEMP-')],
            [sg.Text('Digite a Humidade       '),sg.InputText('',key='-HUM-')],
            [sg.Text('Digite o estado do relé '),sg.InputText('',key='-RELE-')],
            [sg.Button('Adicionar')],
            [sg.Text('')],
            [sg.Text('Dados Registados') ],
            [sg.Listbox(TIMES,size=(50,10),key='-BOX-') ],
            [sg.Button('Apagar'), sg.Button('Sair')]]
        

#front()


#TIME,TEMP,HUM,RELE

# Create the Window
window = sg.Window('Base de Dados de Leitura de Dados', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    button, values = window.read()
    if button == 'Adicionar': # if user closes window or clicks cancel
        ID = randint(1,9999)
        TIMES = values['-TIMES-']
        TEMP = values['-TEMP-']
        HUM = values['-HUM-']
        RELE = values['-RELE-']


        if ID != '':
        #dbase.write(ID,NAME)
            back_gui.write(ID,TIMES,TEMP,HUM,RELE)

        TIMES = back_gui.read_task()

    #faz o reset dos campos para se poder escrever novamente
    #window.find_element('-ID-').Update('')
    window.find_element('-TIMES-').Update('')
    window.find_element('-TEMP-').Update('')
    window.find_element('-HUM-').Update('')
    window.find_element('-RELE-').Update('')
    #window.find_element('-BOX-').Update(ID)
    window.find_element('-BOX-').Update(TIMES)
    #window.find_element('-BOX-').Update(TEMP)
    #window.find_element('-BOX-').Update(RELE)

    if button == 'Apagar':
        if TIMES:
            x=values['-BOX-'][0]
            back_gui.delete(x)
            TIMES = back_gui.read_task()
            window.find_element('-BOX-').Update(TIMES)
    
    #if button == 'Sair':
    if button == 'Sair' or button ==  sg.WIN_CLOSED:
        window.close() 
        break

window.close()