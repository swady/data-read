import numpy as np                  #import numpy libraries
import matplotlib.pyplot as plt     #import matplot libraries




#calling the file path and skipping the first row
#first row contains the column info which is not necessary in the graph

data=np.genfromtxt('G:\\filehandling\\winequality-red.csv',delimiter=';',skip_header=1)



a1=data[1:12,0].max()       #maximum value of the first column
a2=data[1:12,0].min()       #minimum value of the first column
a3=data[1:12,0].mean()      #average value of the first column

b1=data[1:12,1].max()       #maximum value of the second column
b2=data[1:12,1].min()       #minimum value of the second column
b3=data[1:12,1].mean()      #average value of the second column

c1=data[1:12,2].max()       #maximum value of the third column
c2=data[1:12,2].min()       #minimum value of the third column
c3=data[1:12,2].mean()      #average value of the third column

d1=data[1:12,3].max()       #maximum value of the forth column
d2=data[1:12,3].min()       #minimum value of the forth column
d3=data[1:12,3].mean()      #average value of the forth column

e1=data[1:12,4].max()       #maximum value of the fifth column
e2=data[1:12,4].min()       #minimum value of the fifth column
e3=data[1:12,4].mean()      #average value of the fifth column

f1=data[1:12,5].max()       #maximum value of the sixth column
f2=data[1:12,5].min()       #minimum value of the sixth column
f3=data[1:12,5].mean()      #average value of the sixth column

g1=data[1:12,6].max()       #maximum value of the seventh column
g2=data[1:12,6].min()       #minimum value of the seventh column
g3=data[1:12,6].mean()      #average value of the seventh column

h1=data[1:12,7].max()       #maximum value of the eigth column
h2=data[1:12,7].min()       #minimum value of the eigth column
h3=data[1:12,7].min()       #average value of the eigth column


i1=data[1:12,8].max()       #maximum value of the ninth column
i2=data[1:12,8].min()       #minimum value of the ninth column
i3=data[1:12,8].mean()      #average value of the ninth column

j1=data[1:12,9].max()       #maximum value of the tenth column
j2=data[1:12,9].min()       #minimum value of the tenth column
j3=data[1:12,9].mean()      #average value of the tenth column


k1=data[1:12,10].max()      #maximum value of the eleventh column
k2=data[1:12,10].min()      #minimum value of the eleventh column
k3=data[1:12,10].mean()     #average value of the eleventh column

l1=data[1:12,11].max()      #maximum value of the twelth column
l2=data[1:12,11].min()      #minimum value of the twelth column
l3=data[1:12,11].mean()     #average value of the twelth column




m=[a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1]     #arranging the maximum values in a list

n=[a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2]     #arranging the minimum values in a list

o=[a3,b3,c3,d3,e3,f3,g3,h3,i3,j3,k3,l3]     #arranging the avergae values in a list

#ploting the list with legends

p,=plt.plot(m, '--', label='strong wine')       
q,=plt.plot(n, '-', label='low quality wine')
r,=plt.plot(o, '-^', label='average wine quality')
plt.legend(handles=[p,q,r],loc='upper left')


plt.show()
