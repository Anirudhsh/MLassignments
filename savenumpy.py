import numpy as np

st = input("Enter dimension in the form of PxQ where P is rows and Q is cols")
st = st.split("x")
#x = x.astype('int64')
#y = y.astype('int64') 
print(st)
if len(st)!=2:
    print("Enter dimensions in valid format\n")
else:
    rows = int(st[0])
    cols = int(st[1])
    #print(rows+cols)
    rmat=np.random.random((rows,cols))*20
    rmat = rmat.astype('int64') 
    print(rmat)
    #saved in npy format
    np.save('new',rmat)
    #loading the saved numpy array
    np.load('new.npy')
    
