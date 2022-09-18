import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.font_manager as font_manager
import sys 
#axis_font = {'fontname':'Arial', 'size':'14'}

#Fitting function
def func(x, a, b):
      return a + b *  x * x     
      #return a * x + b

#This function is reading data from data-files
def filedata1(path, filename):
    pathfilename = path + filename  
    with open(pathfilename) as f:
        lines = f.readlines()
        r = [line.split()[0] for line in lines]
        u = [line.split()[1] for line in lines]
        return (r, u)

## Enter the input data file to be fitted 
filename = sys.argv[1] #input('Enter the file name: ')
##filename =  'elec-0.1ev.dat'  #'hole-0.1ev.dat'
k = filedata1('./', filename)
#Experimental x and y data points    
xData = np.array(k[0], dtype = float)  # x axis from data
yData = np.array(k[1], dtype = float)  # y axis from data  

#Computing SST 
y_sum = 0.0
n = len(yData)
for y in yData:
	y_sum += y # sum 

y_avg = y_sum/n # average
sst = 0.0
for y in yData:
	sst += (y-y_avg) ** 2           	

print('sst' ,sst)
#sigma = np.zeros((len(xData)), dtype = float)
#print(xData,yData)
#print(type(xData))

#Plot experimental data points
plt.plot(xData, yData, '--o', label='actual-data')

# Initial guess for the parameters
initialGuess = [1.0,1.0]    

#Perform the curve-fit

popt, pcov = curve_fit(func, xData, yData, initialGuess)
##perr = np.sqrt(np.diag(pcov))
r = yData - func(xData, *popt)
sse = 0.0
for ri in r:
	sse += ri*ri

print('sse',sse)
## this is correlatoin coefficient 
r_coeff = np.sqrt(1-sse/sst)
print(r_coeff)

#print(popt) #print(perr)
#x values for the fitted function
xFit = np.arange(xData[0], xData[-1], 0.001)

print(popt)
legend = np.array([popt, r_coeff])
#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='a=%10.6f, b=%10.6f ,r_coeff=%10.6f' % (popt[0], popt[1], r_coeff))
plt.xticks(fontsize=20)
plt.xlabel('T(K)', size = 20)
plt.yticks(fontsize=20)
plt.ylabel('Seebeck (mV/K)', size = 20)
plt.legend(loc = 'upper right')
plt.show()
