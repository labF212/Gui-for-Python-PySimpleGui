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

  
#Default Interface

col11 = [
        [sg.Text(' ', font=('Inder',3), s=(20,1))],
        [sg.Text('Sound Speed',size=(25,2),key=('-SOUNDSPEED-'))],
        [sg.Text('Silent Speed',size=(25,1),key=('-SILENTPEED-'))],
        [sg.Text('*0 for instant',size=(25,2),key=('-0FOR-'))]
        ]

col12 = [
        [sg.Slider((0,2), resolution=0.1,orientation='h', s=(10,15),expand_x=True,key='-SOUNDED-')],
        [sg.Slider((0,2), resolution=0.1,orientation='h', s=(10,15),expand_x=True,key='-SILENT-')]
        ]

col21 = [
        [sg.Text(' ', font=('Inder',5), s=(20,1),expand_x=True)],
        [sg.Text('Frame Margin', s=(25,1),key=('-FMARGIN-'),expand_x=True)],
        [sg.Text('Frame Rate', s=(25,1), pad=(5,17),key=('-FRATE-'),expand_x=True)],
        [sg.Text('Frame Quality', s=(25,2),key=('-FQUAL-'), expand_x=True)],
        [sg.Text('Silent Threashold', s=(25,1),key=('-STHRE-'), expand_x=True)],
        [sg.Text(' ', font=('Inder',1), s=(25,1),expand_x=True)],
        [sg.Text('Sample Rate', s=(25,1), key=('-SRATE-'),expand_x=True)]
        ]

col22 = [
        [sg.Slider((0,10), resolution=1,orientation='h',  s=(10,15),expand_x=True,key='-MARGIN-')],
        [sg.Slider((0,90), resolution=1,orientation='h',  s=(10,15),expand_x=True,key='-RATE-')],
        [sg.Slider((1,30), resolution=1,orientation='h',  s=(10,15),expand_x=True,key='-QUALITY-')],
        [sg.Slider((0,2), resolution=0.01,orientation='h',s=(10,15),expand_x=True,key='-THREASHOLD-')],
        [sg.Text(' ', font=('Inder',5), expand_x=True)],
        [sg.Radio('44100Hz',1, default=True,key='-RAD1-'),sg.Radio('48000Hz', 1,default=False,key='-RAD2-', expand_x=True)]
        ]


layout = [  
        [sg.Text('JumpCutter',justification='c',expand_x=True, font=('Inder',20),pad=(0,5))],
        [sg.Text('Choose your Language:', key='-LANG-',pad=(0,10)),sg.Combo(('English','Português (PT)'), default_value='English',enable_events=True,key='-LANGUAGE-')],
        [sg.HSep()],
        [sg.Text('Input File',justification='c',expand_x=True, font=('Inder',20),pad=(0,5),key='-IN-')],
        [sg.InputText(font=('Inder',10),key='-FILENAME-',expand_x=True),sg.FileBrowse('Choose File',file_types=(("All Files", "*.*"),("Sound Files", "*.wav,*.ogg,*.mp3"),("Movie Files", "*.mpg,*.mp4,*.webm")),tooltip='Local Files')],
        [sg.Text('*If web file PASTE URL to here', key='-URL-')],
        [sg.HSep()],
        [sg.Text('Options',justification='c',expand_x=True, font=('Inder',20), key='-OPTIONS-')],
        [sg.Column(col11),sg.Column(col12,vertical_alignment='top',expand_x=True)],
        [sg.HSep()], 
        [sg.Text('Advanced Options',justification='c',expand_x=True, font=('Inder',20), key='-AOPTIONS-')],
        [sg.Column(col21,vertical_alignment='top'),sg.Column(col22,vertical_alignment='top',expand_x=True)],
        [sg.HSep()],
        [sg.Button('Export',expand_x=True,key='-EXPORT-')],
        [sg.Text('Original by carykh - PySimpleGui by Petr Korda',key='-ORIGINAL-')]
        ]

window = sg.Window('Jumpcutter GUI', layout,resizable=True)



while True:
    event, values = window.read()
    
    #Get Language
    language=str(values['-LANGUAGE-'])
    
    
    if language == 'English':
        window['-LANG-'].update('Choose your Language:')
        window['-IN-'].update('Input File')
        window['-URL-'].update('*If web file PASTE URL to here')
        window['-OPTIONS-'].update('Options')
        window['-SOUNDSPEED-'].update('Sound Speed')
        window['-SILENTPEED-'].update('Silent Speed')
        window['-0FOR-'].update('*0 for instant')
        window['-AOPTIONS-'].update('Advanced Options')
        window['-FMARGIN-'].update('Frame Margin')
        window['-FRATE-'].update('Frame Rate')
        window['-FQUAL-'].update('Frame Quality')
        window['-STHRE-'].update('Silent Threashold')
        window['-SRATE-'].update('Sample Rate')
        window['-ORIGINAL-'].update('Original by carykh - PySimpleGui by Petr Korda')
        window['Choose File'].update('Choose File')
        window['-EXPORT-'].update('Export')
        #'-EXPORT-'
        
    if language == 'Português (PT)':
        window['-LANG-'].update('Escolha a sua linguagem:')
        window['-IN-'].update('Ficheiro de Entrada')
        window['-URL-'].update('*Se for ficheiro da WEB copie o URL para aqui')
        window['-OPTIONS-'].update('Opções')
        window['-SOUNDSPEED-'].update('Velocidade do Som')
        window['-SILENTPEED-'].update('Velocidade do Silêncio')
        window['-0FOR-'].update('*0 se for instantâneo')
        window['-AOPTIONS-'].update('Opções Avançadas')
        window['-FMARGIN-'].update('Margem da Imagem')
        window['-FRATE-'].update('Velocidade das Frames')
        window['-FQUAL-'].update('Qualidade da Imagem')
        window['-STHRE-'].update('Valor de corte Silêncio')
        window['-SRATE-'].update('Tempo de amostragem')
        window['-ORIGINAL-'].update('Original por carykh - PySimpleGui por Petr Korda')
        window['Choose File'].update('Escolha o Ficheiro')
        window['-EXPORT-'].update('Exportar')
        
    #Get File Name
    File_name = str(values['-FILENAME-'])
    
    #Get values of Sliders
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
    
        
    if event=='Export' or event=='Exportar':
              
        text_out=("File Name: " + File_name + "\nSample Rate: " + freq_rad + "\nSound Speed: " + Speed +"\nSilent: "
                  + Silent+"\nMargin: "+Margin+"\nRate: "+Rate+"\nQuality: "+Quality+"\nThreashold: "+Threashold)
        sg.Popup(text_out,title='Resultados',keep_on_top=True)
        
        
   

window.close()