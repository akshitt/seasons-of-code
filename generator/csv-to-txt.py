import pandas as pd
import numpy as np
import csv
fields = []
rows = []

with open('songdata.csv', 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

text = ''
j=0
for i in range(len(rows)):
    if(rows[i][0] == 'The Weeknd'):
        text+=rows[i][3]
        j=j+1
        print(rows[i][1])
        
file = open("lyrics.txt",'w')
file.write(text)
file.close()

print(j)
