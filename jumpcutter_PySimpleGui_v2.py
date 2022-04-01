#https://pysimplegui.readthedocs.io/en/latest/


import PySimpleGUI as sg

#escolha do tema e alterações ao tema
sg.change_look_and_feel('Reddit')
sg.set_options (font=('Courier 12')) 

'''
desenho do layout ou interface
cada [] corresponde a uma linha
cada , dentro das [] correspode a mais um elemento dentro dessa linha
pode-se criar colunas usando sg.Col
'''

layout = [  
        [sg.Text('JumpCutter',justification='c',expand_x=True, font=('Inder',20))],
        [sg.Text('Input File')],
        [sg.InputText(font=('Inder',10),key='-FILENAME-',expand_x=True),sg.FileBrowse('Choose File',tooltip='Local File')],
        [sg.Text('*If web file PASTE URL to here')],
        [sg.HSep()],
        [sg.Text('Options',justification='c',expand_x=True, font=('Inder',20))],
        [sg.Text('Sound Speed'),sg.Slider((0,2), resolution=0.1,orientation='h', s=(10,15),expand_x=True,key='-SOUNDED-')],
        [sg.Text('Silent Speed'),sg.Slider((0,2), resolution=0.1,orientation='h', s=(10,15),expand_x=True,key='-SILENT-')],
        [sg.Text('*0 for instant',font=('Open Sans',10))],
        [sg.HSep()], 
        [sg.Text('Advanced Options',justification='c',expand_x=True, font=('Inder',20))],
        [sg.Text('Frame Margin'),sg.Slider((0,10), resolution=1,orientation='h', s=(10,15),expand_x=True,key='-MARGIN-')],
        [sg.Text('Frame Rate'),sg.Slider((0,90), resolution=1,orientation='h', s=(10,15),expand_x=True,key='-RATE-')],
        [sg.Text('Frame Quality'),sg.Slider((1,30), resolution=1,orientation='h', s=(10,15),expand_x=True,key='-QUALITY-')],
        [sg.Text('Silent Threashold'),sg.Slider((0,2), resolution=0.01,orientation='h', s=(10,15),expand_x=True,key='-THREASHOLD-')],
        [sg.Text('Sample Rate'),sg.Radio('44100Hz',1, default=True,key='-RAD1-'),sg.Radio('48000Hz', 1,default=False,key='-RAD2-')],
        [sg.HSep()],
        [sg.Button('Export',expand_x=True)],
        [sg.Text('Original by carykh - PySimpleGui por Petr Korda'),]
        ]

window = sg.Window('Jumpcutter GUI', layout)






while True:
    event, values = window.read()
    
    #Get File Name
    File_name = str(values['-FILENAME-'])
    
    #Get values of Slideres
    Speed = str(values['-SOUNDED-'])
    Silent = str(values['-SILENT-'])
    Margin = str(values['-MARGIN-'])
    Rate = str(values['-RATE-'])
    Quality= str(values['-QUALITY-'])
    Threashold= str(values['-THREASHOLD-'])
        
    #Get values of radio Buttons    
    if values['-RAD1-'] == True and values['-RAD2-'] == False:
        freq_rad='44100Hz'
    if values['-RAD2-'] == True and values['-RAD1-'] == False:
        freq_rad='48000Hz'
    
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Reset':
        #funcao apagar nome do ficheiro?
        pass
    
        
    if event=='Export':
              
        text_out=("File Name: " + File_name + "\nSample Rate: " + freq_rad + "\nSound Speed: " + Speed +"\nSilent: "
                  + Silent+"\nMargin: "+Margin+"\nRate: "+Rate+"\nQuality: "+Quality+"\nThreashold: "+Threashold)
        sg.Popup(text_out,title='Resultados',keep_on_top=True)
        
        
   

window.close()