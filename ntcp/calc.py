import numpy as np
import pandas as pd
import math

class calc:
    __slots__ = ["fin","geud","ntcp","dvh_arr","a","d50","m"]
    def __init__(self):
        self.fin = {}
        self.geud = {}
        self.ntcp = {}
        self.dvh_arr = {}
        self.a = {}
        self.d50 = {}
        self.m = {}

    def diffDVH2arr(self, fin):
        self.fin =fin
        df = pd.read_excel(self.fin,header=0,index_col=None)
        dose = df.iloc[:,0]
        vol = df.iloc[:,1]
        self.dvh_arr = np.vstack((dose,vol))
        return self.dvh_arr

    def get_geud(self, dvh_arr, a = 23.274):
        self.a = a
        dose = dvh_arr[0,:]
        vol = dvh_arr[1,:]
        sum = 0
        for i,j in zip(dose,vol):
            sum += ((i)**self.a) * j
        self.geud = (sum)**(1/self.a)
        return self.geud

    def get_ntcp(self, dose, d50=6.235, m=0.498):
        self.d50 = d50
        self.m = m
        self.ntcp = 1 / 2 * (1 + math.erf((dose - self.d50) / (self.m * self.d50 * (2 ** (1 / 2)))))
        return self.ntcp





