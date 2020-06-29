import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("/Users/evancosta/Desktop/DataParse2/12-13.csv") 
data = data.dropna(axis=1, how='all')

index = []
count = 0
for x in data.columns:
    if 'Unnamed' in x:
        data.iloc[:, count]
    else:
        index.append('alpha')
        index.append(x)
    count += 1
data.columns = index

data = data.loc[:,~data.columns.duplicated()]
data = data.drop([0])
datarr = data.to_numpy(dtype=float)
datarr = datarr[1: datarr.shape[0]]

change = 0
for i in range(1, len(datarr[0, :])):
    holder = []
    for x in range(len(datarr[:, i])-1):
        if change != 0:
            datarr[x][i] += change 
        else: 
            difference = datarr[x][i] - datarr[x+1][i]
            if abs(difference) > 0.1:
                    change = difference
        change = 0
        
plt.plot(datarr[:,2])
#thirtyten = np.subtract(csvmat[:,7], csvmat[:,1])
#plt.plot(thirtyten)
plt.show()

'''
with open('12-13.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #csvmat = createmat(csv_reader)
    csvmat = np.zeros((802, 16))
    line_row = 0
    print(csv_reader)
    row2 = 0
    for row in csv_reader:
        if line_row > 1 and line_row < 802:
            if row:
                line_col = 0
                for col in row:
                    if line_col < len(csvmat[0,:]):
                        csvmat[row2][line_col] = col
                        line_col += 1
                row2 += 1                
        line_row += 1

    print(csvmat)
'''
 
    
