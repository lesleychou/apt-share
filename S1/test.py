import numpy as np

a = [0.64,0,0,0.32,0]
b= np.zeros(6)
res = [idx for idx, val in enumerate(a) if val > 0.5]
b[res]=1
print(b)
a.extend(b)
print(a)