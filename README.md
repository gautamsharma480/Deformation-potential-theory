# Deformation-potential-theory
electron-phonon relaxation time calculator from Deformation potential theory

These codes (clean-cubic.py, quadratic.py and me-calculator.f90) calculate effective masses by fitting the  valence band maximum (VBM), and conduction band minimum (CBM).  
me-calculator.f90 is needed if you use Quantum ESPRESSO to calculate the band structures. This takes into account of x-axis units for the band structure.
If the parabola (VBM, CBM) is situated at the origin, then use quadratic.py 
If the parabola (VBM, CBM) is shifted from the origin, then use clean-cubic.py (shifted parabola equation is used to fit the energy)
