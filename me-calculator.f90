program me_calculator


real::a1,me,alat
real::a11   !! a1 in units of Joule/m^2
real*8,parameter :: hcut = 6.5821*1e-16 !!eV s
real*8, parameter :: pi = 3.1415926
print*,"Give a1"
read*,a1
!!!!a1 has units of ev/k^2
alat = 13.798132882*0.529177249*1e-10  ! in meters

a11 = ((a1*1.602*1e-19)*(alat*alat))/(4*pi*pi)  !1!! Joule/meter^2

!!!!!!  1.602*1e-19*1.602*1e-19 = 2.566404*1e-38

me = 0.500000*((hcut*hcut*2.566404*1e-38)/a11)
me=me/(9.10938356*1e-31)
print*,"me(unit of me)",me


end program
 
