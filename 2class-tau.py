import math
import numpy as np 
import sys 
#this code requires the input of temperature, elastic constant (C), deformation potential constant (E_dp) and effective mass (m*) of the carrier.
# Accepted units (Kelvin, eV/A^3, eV, unit of mass of electron)
# Elastic constant (C can have different units (C_3D or C_2D), depending on the dimensionality of the material.)
# Same code can be used to calculate relaxation time in two-dimension, only expression for tau will change.
class R_tau:

	def __init__(self,T,C,E_dp,m):
		self.T = T
		self.C = C
		self.E_dp = E_dp
		self.m = m

	@property
	def tau(self):
		pi = 3.1415926
		ev = 1.60218e-19  # Joule
		me = 9.10938356e-31 # Kg
		kBT = 1.380649e-23*self.T # Joule/K * K = Joule
		h_cut = 1.054571817e-34 # Joule sec
		h_cut_cube = h_cut ** 3   # Joule^3  sec^3
		h_cut_four = h_cut ** 4
		angstrom = 1e-10 #meter
		angstrom_sq = angstrom**2  #meter
		md_e = self.m * me # random
		self.C = self.C * ev / 1e-30 # Joule/m^3
		self.E_dp = self.E_dp * ev   # Joule 
		num = (2 * math.sqrt(2*pi) * h_cut_four * self.C)
		deno = (3 *  ((kBT  * md_e) ** 1.5) * self.E_dp**2)
		tau   =  num / deno # This is for 3D system # npj Computational Materials (2020) 6:149 
		# in case, you need to compute relaxation time in 2-dimensional system
		#tau_2d = (h_cut_cube * self.C) / ( kBT  * md_e *  self.E_dp ** 2) # Journal of Electronic Materials volume 50, 1644–1654 (2021)
		return tau / 1e-15 # fs

	def c_3d(self,vol,a2):
		ry2ev = 13.605698066
		bohr2anstrom = 0.529177249
		bohr2anstrom3 = bohr2anstrom ** 3
		self.vol = vol * bohr2anstrom3  # angs^3
		self.a2 = a2
		c_3d = 2*self.a2*ry2ev/self.vol
		print('c_3d (eV/A^3)', c_3d)
		return c_3d  # eV/A^3 


#c_3d = c.c_3d(1100,10)

tau_e = R_tau(300,11,10,2) # (Kelvin, eV/A^3, eV, unit of mass of electron)
print(tau_e.tau)

