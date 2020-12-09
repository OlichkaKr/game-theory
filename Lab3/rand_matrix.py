import random
import numpy as np

m = 3
n = 2
C1 = -40
C2 = -25

G = np.array([[random.randint(C1, C2) for j in range(n)] for i in range(m)]).reshape(m, n)

print(G)

maxmin = max(G.min(axis=1))
minmax = min(G.max(axis=0))

print(maxmin)
print(minmax)

if maxmin != minmax:
    print('No settle point')
else:
    xy = np.where(G == maxmin)
    settle = list(zip(*xy))
    
    for i in settle:
        if G[i] == max(G[:,i[1]]):
            print('Settle point is (i0 = {}, j0 = {})'.format(i[0], i[1]))