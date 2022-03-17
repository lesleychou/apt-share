import numpy as np
aa=[1,2,3,4,5]
a = [0.64,0,0,0.32,0]
b= np.zeros(6)
res = [idx for idx, val in enumerate(a) if val == 0]
b[res]=1
aa=np.array(aa)

print(res)
print(aa[res[0:int(len(res)*0.8)]])
#aa=list(aa[res[0:int(len(res)*0.8)]])
print(aa)
a.extend(list(aa[res[0:int(len(res)*0.8)]]))
print(a)