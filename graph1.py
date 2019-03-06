import numpy as np                  #import numpy libraries
import matplotlib.pyplot as plt     #import matplot libraries


#path of the file
#store the fetched data into data variable
data=np.genfromtxt('G:\\filehandling\\winequality-red.csv',delimiter=';',skip_header=1)


#title and lables in the plot

plt.title('Wine quality')
plt.xlabel('number of data')
plt.ylabel('number of units')



#storing the column values into the variables

a=data[1:12,0]          
b=data[1:12,1]
c=data[1:12,2]
d=data[1:12,3]
e=data[1:12,4]
f=data[1:12,5]
g=data[1:12,6]
h=data[1:12,7]
i=data[1:12,8]
j=data[1:12,9]
k=data[1:12,10]
l=data[1:12,11]


#ploting the values with the legends of respective label

m, = plt.plot(a,'->', label='fixed acidity')
n, = plt.plot(b,'-o', label='volatile acidity')
o, = plt.plot(c,'--', label='Citric acid')
p, = plt.plot(d,'-^', label='Resudial Sugar')
q, = plt.plot(e,'-', label='chlorides')
r, = plt.plot(f,'--', label='free sulfur dioxide')
s, = plt.plot(g,'-', label='Total sulfur dioxide')
t, = plt.plot(h,'-o', label='Density')
u, = plt.plot(i,'->', label='pH')
v, = plt.plot(j,'-+', label='Sulphate')
w, = plt.plot(k,'-+' 'r', label='alcohol')
x, = plt.plot(l,'-o', label='wine quality')
plt.legend(handles=[m,n,o,p,q,r,s,t,u,v,w,x],loc='upper left')

plt.show()
