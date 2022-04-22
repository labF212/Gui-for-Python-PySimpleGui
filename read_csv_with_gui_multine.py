# coding=utf-8
#https://www.programcreek.com/python/?project_name=PySimpleGUI%2FPySimpleGUI#

import PySimpleGUI as sg
import csv
#import pandas as pd

rows = []
filename =''

layout =[
        [sg.Text("Escolha o ficheiro que deseja abrir")],
        [sg.Input(key='-IN-', expand_x=True),sg.FileBrowse(file_types=(("CSV Files","*.csv"),("All Files","*.*",)))],
        [sg.Multiline(key='-DATA-', size=(35,10),autoscroll= True, expand_y=True, expand_x=True)],
        
        [sg.Push(),sg.Button('Some data',key='-SHOW-'),sg.Button('All Data',key='-ALL-'),sg.Button('CLEAR'), sg.Button('EXIT'),sg.Push()]
        ]

window = sg.Window('My CSV File',layout,resizable=True)


while True:
    event,values=window.read()
    filename =str(values['-IN-'])
    
    if event in (sg.WIN_CLOSED,"EXIT"):
        window.close()
        break
    
    if event =='CLEAR':
        window['-IN-'].Update('')
        window['-DATA-'].Update('')
        
    
    if event =='-SHOW-' and filename!='':
    
        with open(filename,"r") as file:
            csvreader = csv.reader(file)
            header=next(csvreader)
            for row in csvreader:
                rows.append(row)

        #print all data       
        print(header)
        print(rows)
        
        #PRINT data on GUI       
        window['-DATA-'].Update(header[2]+'   '+header[3]+'\n',append=True) #print Header om GUI
        for i in range(len(rows)): #reads temperatures and humiditys
            window['-DATA-'].Update('        '+rows[i][2]+'                '+rows[i][3]+'\n',append=True)
        
        file.close

    if event =='-ALL-' and filename!='':
        #open and reads data from file
        with open(filename,"r") as file:
            csvreader = csv.reader(file)
            header=next(csvreader)
            for row in csvreader:
                rows.append(row)
        
        
        
        for i in range(len(header)): #reads header
            window['-DATA-'].Update('    '+ header[i] +'   ',append=True) #print Header om GUI
        window['-DATA-'].Update('\n',append=True)
        for i in range(len(rows)): #reads data
            for j in range(len(header)):
                window['-DATA-'].Update('        '+rows[i][j]+'        ',append=True)
                if j==len(header)-1:
                    window['-DATA-'].Update('\n',append=True)
        file.close 

window.close()


