import numpy as np
import pandas as pd
import math

def diffDVH2arr(fin):
    df = pd.read_excel(fin,header=0,index_col=None)
    dose = df.iloc[:,0]
    vol = df.iloc[:,1]
    arr = np.vstack((dose,vol))
    return arr

def geud(dvh_arr):
    a = 23.274
    dose = dvh_arr[0,:]
    vol = dvh_arr[1,:]
    sum = 0
    for i,j in zip(dose,vol):
        sum += ((i)**a) * j
    sol = (sum)**(1/a)
    return sol

def ntcp(dvh_arr):
    d50 = 6.235
    m = 0.498
    dose = geud(dvh_arr)
    ntcp = 1 / 2 * (1 + math.erf((dose - d50) / (m * d50 * (2 ** (1 / 2)))))
    return ntcp




fin = "cum.xlsx"



