import csv
#import pandas as pd

rows = []

with open("data_csv.csv","r") as file:
    csvreader = csv.reader(file)
    header=next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
print(rows[1][2])

print(header[2],header[3])
for i in range(len(rows)): #read only temperature
    
    print(rows[i][2],rows[i][3])



file.close

'''
data=pd.read_csv('data_csv.csv')
data.Temperatura
'''

