import numpy as np
a = np.arange(12).reshape(3,4)
b = a > 4; print(b)
print(a[b])
a[b] = 0 ; print(a)
a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])
b2 = np.array([True,False,True,False])
print(a[b1,:]); print(a[b1])
print(a[:,b2]); print(a[b1,b2])
print('#',50*"-")