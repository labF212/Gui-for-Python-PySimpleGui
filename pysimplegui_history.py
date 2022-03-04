# coding=utf-8
from random import randint
import threading
import PySimpleGUI as sg
import sys
from webbrowser import open
from time import *
#from datetime import datetime

sg.change_look_and_feel('DarkGrey')


#cores dos gráficos
bcols = ['grey','red','yellow','black','white','blue']

#Gráfico do Histórico
STEP_SIZE = 1  # can adjust for more data saved than shown
SAMPLES = 100 # number of point shown on the chart
SAMPLE_MAX = 100 # high limit of data points
CANVAS_SIZE = (300, 110)
LABEL_SIZE = (300,20)


timebar = sg.Graph(LABEL_SIZE, (0, 0),(SAMPLES, 20), background_color=bcols[4], key='-TIMEBAR-',expand_x=True)
history = sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),background_color=bcols[0], key='-HISTORY-',expand_x=True)

# create an array of time and data value
pt_values = []
pt_times = []
for i in range(SAMPLES+1): 
    pt_values.append("")
    pt_times.append("")


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
        sg.Column(col13,expand_x=True,vertical_alignment='bottom'),sg.Column(col14,expand_x=True,vertical_alignment='bottom')],
        [sg.HSep()],
        [sg.Text('Hora Atual:'),sg.Text('00:00:00',expand_x=True,key='-HORA-'),sg.Text('Data:'),sg.Text('00/00/0000',expand_x=True,key='-DATA-')]
        
        ]

left_box=[ 
        [sg.Image(r'redon.png',tooltip='Estado do Relé',key='-RELE-')],
        [sg.Text('Estado do Relé:'),sg.Text(' ',key='-TRELE-')],
        [sg.HSep()]
        ]
right_box= [
        [sg.Text('Configuração de limites do sensor de Humidade',expand_x=True,justification='center')],
        [sg.Text(' ')],
        [sg.Text('Valor minimo: '),sg.Spin(initial_value=70, values=list(range(50,100)), enable_events=True,size=(5,5),key='-MAXSPIN-')],
        [sg.Text('Valor maximo:'),sg.Spin(initial_value=30, values=list(range(0,50)), enable_events=True,size=(5,5),key='-MINSPIN-')],
        #[sg.Spin((0,100),initial_value=20,enable_events=True)]
        [sg.HSep()],
        [sg.Text('Registo do Histórico dos dados',expand_x=True,justification='center')],
        [sg.Quit(button_color=('white', 'red')),sg.Button(button_text="Print Log", button_color=('white', 'green'),key="log"),
         sg.Text('     ',  key='-OUTPUT-',text_color=bcols[1]),sg.Text('     ',  key='-OUTPUT1-',text_color=bcols[5])],
        [history],
        [timebar], 
        ]

layout = [  
            [sg.Menu(menu_def,tearoff=True)], #menu
            
            [sg.Frame('   Leitura de Dados   ',frame_sup,font='15',expand_x=True,title_location='n')],
           
           # [sg.Button('Ok'), sg.Button('Cancel'))] ]
           [sg.Text('Tratamento de dados',expand_x=True,justification='center',font='15') ],[sg.HSep()],
           [sg.Column(left_box,expand_x=True),sg.Column(right_box,expand_x=True)]
           
           ]


def update():
    while 1:
        sleep(1)
        #ver tabela de letras que correspodem ao formato do relogio
        #https://www.programiz.com/python-programming/datetime/strftime
        time_string = strftime("%H:%M:%S")
        #time_label.config(text=time_string)
        
            
        #date_string = strftime("%d %B %Y") dia mes ano
        date_month = strftime("%B")
        months_eng =   ["January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"]
        meses_pt = ["Janeiro",
                    "Fevereiro",
                    "Março",
                    "Abril",
                    "Maio",
                    "Junho",
                    "Julho",
                    "Agosto",
                    "Setembro",
                    "Outubro",
                    "Novembro",
                    "Dezembro"]
        
        months_day_len = len (months_eng)
        
        for f in range (0,months_day_len):
            if date_month == months_eng[f]:
                date_month = meses_pt[f]
                
        date_string = strftime("%d ") + date_month + strftime(" %Y")
        window['-HORA-'].update(time_string)
        window['-DATA-'].update(date_string)




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
time_string=window['-HORA-']
date_string = window['-DATA-']
history = window['-HISTORY-']
output  = window['-OUTPUT-']
output1  = window['-OUTPUT1-']

threading.Thread(target=update).start()

i=0
prev_x,prev_y=0,0

# Event Loop to process "events" and get the "values" of the inputs
while True:
    temp = randint(0,45)
    hum =  randint(0,100)
    event, values = window.read(timeout=2000)
    print('buton event',event)
    
    if event == 'link':
        open(githublink)

    if event == 'Sobre': # if user closes window or clicks cancel
        #second_window()
        #threading.Thread(target=second_window).start()
        second_window()
        #sg.popup('Este programa demonstra PySimplePy',title='Sobre')
        print(values)   
    
    if event == 'Sair': # if user closes window or clicks cancel
        window.close()
        sys.exit()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event in ('Quit', None):
        break

    if event == 'log':
        print("\nReal Time Data\n")
        for j in range (SAMPLES+1):
            if pt_times[j] =="":
                break
            print (pt_times[j],pt_values[j])

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
 

    #Get data point and time
    data_pt1  =   temp
    data_pt2 = hum
    
    now_time = strftime("%H:%M:%S")
    
    #update the point arrays
    pt_values[i]=data_pt1
    pt_times[i]=str(now_time)

    window['-OUTPUT-'].update(data_pt1)
    window['-OUTPUT1-'].update(data_pt2)

    if data_pt1 > SAMPLE_MAX:
        data_pt1 = SAMPLE_MAX
    new_x, new_y = i, data_pt1
    if data_pt2 > SAMPLE_MAX:
        data_pt2 = SAMPLE_MAX
    new_x2, new_y2 = i, data_pt2


    if i >= SAMPLES:
        # shift graph over if full of data
        history.move(-STEP_SIZE, 0)
        prev_x = prev_x - STEP_SIZE
        # shift the array data points
        for i in range(SAMPLES):
            pt_values[i] = pt_values[i+1]
            pt_times[i] = pt_times[i+1]
                    
    history.draw_line((prev_x, prev_y), (new_x, new_y), color='red')
    history.draw_line((prev_x, prev_y), (new_x2, new_y2), color='blue')    
    
    prev_x, prev_y = new_x, new_y
    i += STEP_SIZE if i < SAMPLES else 0
    
        
    timebar.erase()
    # add a scrolling time value 
    time_x = i
    timebar.draw_text(text=str(now_time), location=((time_x - 2),7) )
    # add some extra times
    if i >= SAMPLES:
        timebar.draw_text(text=pt_times[int(SAMPLES * 0.25)], location=((int(time_x * 0.25) - 2),7) )
        timebar.draw_text(text=pt_times[int(SAMPLES * 0.5)], location=((int(time_x * 0.5) - 2),7) )
        timebar.draw_text(text=pt_times[int(SAMPLES * 0.75)], location=((int(time_x *0.75) - 2),7) )
    if i > 10:
        timebar.draw_text(text=pt_times[1], location=( 2,7) )
    
    progress_temp_bar.UpdateBar(temp)
    progress_temp_hum.UpdateBar(hum)
    window['-TEXTTEMP-'].update(str(temp) + 'ºC')
    window['-TEXTHUM-'].update('    ' + str(hum) + '%')
    

window.close()