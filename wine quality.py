import numpy as np
import matplotlib.pyplot as plt


data=np.genfromtxt('G:\\filehandling\\winequality-red.csv',delimiter=';',skip_header=1)


print('average fixed acid in wine = ',data[:,0].mean())
print('max fixed acid = ',data[:,0].max())
print('min fixed acid = ',data[:,0].min())
print('\n')
print('average volatile acid in wine = ',data[:,1].mean())
print('max volatile acid in wine = ',data[:,1].max())
print('min volatile acid in wine = ',data[:,1].min())
print('\n')
print('average citric acid in wine = ',data[:,2].mean())
print('max citric acid in wine = ',data[:,2].max())
print('min citric acid in wine = ',data[:,2].min())
print('\n')
print('average residual sugar in wine = ',data[:,3].mean())
print('max residual sugar in wine = ',data[:,3].max())
print('min residual sugar in wine = ',data[:,3].min())
print('\n')
print('average chlorides in wine = ',data[:,4].mean())
print('max chlorides in wine = ',data[:,4].max())
print('min chlorides in wine = ',data[:,4].min())
print('\n')
print('average free sulfer dioxide in wine = ',data[:,5].mean())
print('max free sulfer dioxide in wine = ',data[:,5].max())
print('min free sulfer dioxide in wine = ',data[:,5].min())
print('\n')
print('average total sulfar dioxide in wine = ',data[:,6].mean())
print('max total sulfar dioxide in wine = ',data[:,6].max())
print('min total sulfar dioxide in wine = ',data[:,6].min())
print('\n')
print('average density in wine = ',data[:,7].mean())
print('max density in wine = ',data[:,7].max())
print('min density in wine = ',data[:,7].min())
print('\n')
print('average pH value of wine = ',data[:,8].mean())
print('max pH value in wine = ',data[:,8].max())
print('min pH value in wine = ',data[:,8].min())
print('\n')
print('average sulphates in wine = ',data[:,9].mean())
print('max sulphates in wine = ',data[:,9].max())
print('min sulphates in wine = ',data[:,9].min())
print('\n')
print('average alcohol in wine = ',data[:,10].mean())
print('max alcohol in wine = ',data[:,10].max())
print('min alcohol in wine= ',data[:,10].min())
print('\n')
print('average quality in wine = ',data[:,11].mean())
print('strong quality wine = ',data[:,11].max())
print('low quality wine = ',data[:,11].min())



















