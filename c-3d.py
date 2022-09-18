

import numpy as np 
import sys
# This code is for three-dimensional system.
# a2 (in Ry) is coefficient obtained by fitting the total energy as a function of strain. 
# Mathematically, (E_total = a0 + a1*x + a2*x^2), where x is strain.
a2  = float(sys.argv[1])
ry2ev = 13.605698066  
bohr2anstrom =0.529177249  
bohr2anstrom3 = bohr2anstrom ** 3 
# Instead of 100 below, put the value of volume (in bohr^3) for your system.
vol =  100 * bohr2anstrom3 * # angs^3  

c_3d = 2*a2*ry2ev/vol 

print('c_3d (eV/A^3)', c_3d) 
