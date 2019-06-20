import matplotlib.pyplot as plt
import pandas as pd
#reading from file
ff=pd.read_csv('datam.csv')
print(ff)
names=ff['student_name'].values
smarks=ff['marks'].values
#plotting pie chart
plt.pie(smarks,labels=names)
plt.show()
