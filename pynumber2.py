import numpy as np
#-------- method 1 -------
#Generating a random number b/w 100 and 125 inclusive
x=int(np.random.random()*25) + 100
print(x)
#creating a full mat with that no.
newm=np.full((8,2),x)
for i in range(8):
    for j in range(2):
        if i==0 and j==0:
            continue
        elif j!=0:
            newm[i][j]=newm[i][j-1]+5
        else:
            newm[i][j]=newm[i-1][1]+5
print(newm)       
# -------- method 2 ----------
#using x and arange fxn then reshaping into 8x2 mat
newm2=np.arange(x,x+16*5,5).reshape(8,2)
print(newm2)
