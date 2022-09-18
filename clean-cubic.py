import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.font_manager as font_manager
import sys 
#axis_font = {'fontname':'Arial', 'size':'14'}

#Fitting function
def func(x, a, b, c, d):
##def func(x, a, b):
      d = 0 # will makes it quadratic functions 
      return a + b * x + c * x * x + d * x * x * x    
      #return a * x + b

def columns2row(path, filename):
    pathfilename = path + filename  
    with open(pathfilename) as f:
        lines = f.readlines()
        r = [line.split()[0] for line in lines]
        u = [line.split()[1] for line in lines] 
        return (r, u)
filename = sys.argv[1] #input('Enter the file name: ')
k = columns2row('./', filename) # function being CALLED, name and path of file passed in
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

#print('sst' ,sst)
#Plot experimental data points
plt.plot(xData, yData, '--o', label='actual-data')

# Initial guess for the parameters
initialGuess = [1.0,1.0,1.0,1.0]   # for all fitting coeffs. 

#Perform the curve-fit
popt, pcov = curve_fit(func, xData, yData, initialGuess, absolute_sigma=True)
print('optimized parametes = ',popt) ## it contains fitted a,b,c values
r = yData - func(xData, *popt) ## yData - yFit
sse = 0.0
for ri in r:
	sse += ri*ri
print('sse',sse)
print('sst' ,sst) # computed earlier 
r_coeff = np.sqrt(1.0 - sse/sst) #this is correlation coeff
print(r_coeff)

#print(popt) #print(perr)
#x values for the fitted function
##print('xData[0_-1]',xData[0], xData[-1])
#xData[0] is first and xData[-1] is last element of array
xFit = np.arange(xData[0], xData[-1], 0.0001)
#same can be achieved as following:
#xFit = linspace(xData[0],xData[-1])

print(popt)
legend = np.array([popt, r_coeff])
#Plot the fitted function
plt.plot(xFit, func(xFit, *popt), 'r', label='a=%10.6f, b=%10.6f ,c=%12.10f, r_coeff=%10.6f' % (popt[0], popt[1], popt[2], r_coeff))
plt.xticks(fontsize=20)
plt.xlabel('electron wave vector(k)', size = 20)
plt.yticks(fontsize=20)
plt.ylabel('Energy (eV)', size = 20)
plt.legend(loc = 'upper right')
plt.show()
