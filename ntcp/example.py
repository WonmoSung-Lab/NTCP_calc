from calc import calc
'''
c = calc()
arr = c.diffDVH2arr("7.xlsx") # arr = [[dose],[volume]]
c.get_geud(c.dvh_arr) # default a = 23.274 /when a is set to 1, it is equal to mean dose.
c.get_ntcp(c.geud) # default d50 = 6.235, m = 0.498
print(c.ntcp)
'''
'''
from calc import calc
import matplotlib.pyplot as plt

# ntcp whole curve plot
c2 = calc()
x = range(0,20)
y = [c2.get_ntcp(i) for i in x]
plt.plot(x,y)
plt.xlabel("Dose [Gy]")
plt.ylabel("Normal tissue complication probability")
plt.show()
'''