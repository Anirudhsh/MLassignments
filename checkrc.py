import numpy as np

#taking row and coloumn input from user
row = int(input("Enter No. Of Rows"))
cols = int(input("Enter No. Of Coloumns"))

#setting range for "FOR"
f = max(row,cols)
for i in range(1,f+1):
#Printing zero matrices for the results thus obtained
    if row%i==0 and cols%i==0:
        print(np.zeros((i,i)))
