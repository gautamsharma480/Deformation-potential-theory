

import numpy as np 
import sys
# a2 (in Ry) is coefficient obtained by fitting the total energy as a function of strain. 
# Mathematically, (E_total = a0 + a1*x + a2*x^2), where x is strain.
a2  = float(sys.argv[1])
ry2ev = 13.605698066  
bohr2anstrom =0.529177249  
celldm = 13.7981*bohr2anstrom 

area = 0.5*np.sqrt(3)*celldm*celldm # for hexagonal system

c_2d = 2*a2*ry2ev/area

print('c_2d (eV/A^2)', c_2d) 
