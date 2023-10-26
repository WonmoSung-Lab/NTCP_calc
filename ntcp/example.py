''' Instruction on how to get ntcp
    please check dvh_example format '''
from calc import calc

c = calc()
arr = c.diffDVH2arr("dvh_example.xlsx")                 # arr = [[dose],[volume]]
c.get_geud(c.dvh_arr, a=23.274)                         # default a = 23.274 /when a is set to 1, it is equal to mean dose.
c.get_ntcp(c.geud, d50=6.235)                           # default d50 = 6.235, m = 0.498
print(c.ntcp)                                           # ntcp of example = 0.88915


'''ntcp plot'''
from calc import calc
import matplotlib.pyplot as plt

c2 = calc()
x = range(0,20)
y = [c2.get_ntcp(i) for i in x]
plt.plot(x,y)
plt.xlabel("Dose [Gy]")
plt.ylabel("Normal tissue complication probability")
plt.show()
