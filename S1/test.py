import numpy as np
aa=[1,2,3,4,5]
a = [0.64,0,0,0.32,0]
c = np.asarray(a)
c = np.asarray(c)
b= np.zeros(6)
for i in a:
    if i == 0:
        del i
del a[2]
print(c)
print(a)
c=c.tolist()
print(c)
res = [idx for idx, val in enumerate(a) if val == 0]
b[res]=1
aa=np.array(aa)

#print(res)
#(aa[res[0:int(len(res)*0.8)]])
#aa=list(aa[res[0:int(len(res)*0.8)]])
#print(aa)
a.extend(list(aa[res[0:int(len(res)*0.8)]]))
#print(a)