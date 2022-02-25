from cgitb import enable
from random import randint
#from turtle import left, right
import PySimpleGUI as sg
import sys
from webbrowser import open

sg.change_look_and_feel('DarkGrey')

#led='redon.png'


#Menus

menu_def= [['&Menu',['S&obre','&Sair']]]

#tray = sg.SystemTray(menu=menu_def,filename='ico.png')

col11 = [
    [sg.Image(r'temperatura.png',expand_x=True)],
    [sg.Text('Temperatura',expand_x=True,justification='center')]
    ]
col12 = [
    [sg.ProgressBar(100, orientation='v', size=(14,50), bar_color="grey", key='progressbar_temp',expand_x=True)],
    [sg.Text('ºC',expand_x=True,key='-TEXTTEMP-',justification='center',auto_size_text=True)]
    ]

col13 = [
    [sg.Image(r'humidade.png',expand_x=True)],
    [sg.Text('Humidade',expand_x=True,justification='center')]
    ]
col14 = [
    [sg.ProgressBar(100, orientation='v', size=(14,50), bar_color="grey", key='progressbar_hum',expand_x=True)],
    [sg.Text('--%',expand_x=True,key='-TEXTHUM-',justification='center')]
    ]

frame_sup = [
        [sg.Column(col11,expand_x=True,vertical_alignment='bottom'),sg.Column(col12,expand_x=True,vertical_alignment='bottom'),
        sg.Column(col13,expand_x=True,vertical_alignment='bottom'),sg.Column(col14,expand_x=True,vertical_alignment='bottom')]

        ]

left_box=[ 
        [sg.Image(r'redon.png',tooltip='Estado do Relé',key='-RELE-')],
        [sg.Text('Estado do Relé:'),sg.Text(' ',key='-TRELE-')],
        [sg.HSep()]
        ]
right_box= [
        [sg.Text('Valor minimo: '),sg.Spin(initial_value=70, values=list(range(50,100)), enable_events=True,size=(5,5),key='-MAXSPIN-')],
        [sg.Text('Valor maximo:'),sg.Spin(initial_value=30, values=list(range(0,50)), enable_events=True,size=(5,5),key='-MINSPIN-')],
        #[sg.Spin((0,100),initial_value=20,enable_events=True)]
        [sg.HSep()]
        ]

layout = [  
            [sg.Menu(menu_def,tearoff=True)], #menu
            
            [sg.Frame('   Leitura de Dados   ',frame_sup,font='15',expand_x=True,title_location='n')],
           
           # [sg.Button('Ok'), sg.Button('Cancel'))] ]
           [sg.Text('Tratamento de dados',expand_x=True,justification='center',font='15') ],[sg.HSep()],
           [sg.Column(left_box,expand_x=True),sg.Column(right_box,expand_x=True)]
           
           ]


def second_window(): #about
    githublink='https://github.com/labF212/PySimpleGui'
    layout = [
        [sg.Text('Tratamento de dados')],
        [sg.Text('versão 1.0'),sg.Text('Fev 2022')],
        [sg.Text('Código em: '),sg.Text('https://github.com/labF212/PySimpleGui',font='font 12 italic underline',text_color='blue',tooltip='https://github.com/labF212/PySimpleGui', enable_events='True',key='link')],
        [sg.Button('Ok',key='-OKSOBRE-')]
               ]
    
               
    window = sg.Window('Sobre',layout,finalize=True)
    
    event,values=window.read()
    
    
    if event == 'link':
        open(githublink)
        window.close()
        second_window()
    if event == sg.WIN_CLOSED or event == '-OKSOBRE-':
        window.close()
    #window.close() 

# Create the Window
window = sg.Window('Leituras de Temperaturas e Humidade', layout,titlebar_icon='ico.png',resizable=True,use_custom_titlebar=False,scaling=True,background_color=None)
progress_temp_bar=window['progressbar_temp']
progress_temp_hum=window['progressbar_hum']
#rele_state=window['-RELE-']

# Event Loop to process "events" and get the "values" of the inputs
while True:
    temp = randint(0,45)
    hum =  randint(0,100)
    event, values = window.read(timeout=2000)
    print('buton event',event)
    
    if event == 'link':
        open(githublink)

    if event == 'Sobre': # if user closes window or clicks cancel
        second_window()
        #sg.popup('Este programa demonstra PySimplePy',title='Sobre')
        print(values)   
    
    if event == 'Sair': # if user closes window or clicks cancel
        window.close()
        sys.exit()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('buton event',event)
    print('You entered ', values[0])
    val_min=int(values['-MINSPIN-'])
    val_max=int(values['-MAXSPIN-'])

    print(hum,val_min)
    if hum < val_min:
        print("Fora do limite")
        #progress_temp_hum.UpdateBar(hum)
        window['-RELE-'].update(r'redoffline.png')
        window['-TRELE-'].update('Desligado')
            #green_label.config(text="Fora do limite")
            #GreenLedImage = PhotoImage(file='redoffline.png')
    elif hum >= val_min and hum <= val_max:
            #green_label.config(text="OK")
            #GreenLedImage = PhotoImage(file='greenledon.png')
        window['-RELE-'].update(r'redon.png')
        window['-TRELE-'].update('Ligado')
        print("OK")
    else:
            #green_label.config(text="Humidade Elevada")
            #GreenLedImage = PhotoImage(file='greenledoff.png')
        window['-RELE-'].update(r'redoff.png')
        window['-TRELE-'].update('Ligado')
        print("Humidade Elevada")
 

    progress_temp_bar.UpdateBar(temp)
    progress_temp_hum.UpdateBar(hum)
    window['-TEXTTEMP-'].update(str(temp) + 'ºC')
    window['-TEXTHUM-'].update('    ' + str(hum) + '%')
    

window.close()