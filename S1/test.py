import random

import numpy as np
aa=[1,2,3,4,5]
a = [0.64,0,0,0.32,0]

res = [idx for idx, val in enumerate(a) if val == 0]
print(res)
random_res = random.sample(res,2)
print(random_res)
res = [ele for ele in res if ele not in random_res]
print(res)

#print(res)
#(aa[res[0:int(len(res)*0.8)]])
#aa=list(aa[res[0:int(len(res)*0.8)]])
#print(aa)

#print(a)