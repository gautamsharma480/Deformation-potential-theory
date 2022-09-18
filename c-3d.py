

import numpy as np 
import sys

a2  = float(sys.argv[1])
ry2ev = 13.605698066  
bohr2anstrom =0.529177249  
bohr2anstrom3 = bohr2anstrom ** 3 
vol =  100 * bohr2anstrom3 * # angs^3  

c_3d = 2*a2*ry2ev/vol 

print('c_3d (eV/A^3)', c_3d) 
