from calc import calc

c = calc()
arr = c.diffDVH2arr("7.xlsx")
geud = c.get_geud(arr) # default a = 23.274
ntcp = c.get_ntcp(geud) # default d50 = 6.235, m = 0.498
print(ntcp)