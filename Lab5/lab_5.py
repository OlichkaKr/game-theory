import random
import numpy as np
from scipy.optimize import linprog
# from math import 

m = 3
n = 5
C1 = -4
C2 = 5

A = np.array([[4, -3, 3, 0, 2], [-3, 5, 2, -4, 3], [5, 1, -1, -3, -2]]).reshape(m, n)

print(A)

maxmin = max(A.min(axis=1))
minmax = min(A.max(axis=0))

print('Maxmin =', maxmin)
print('Minmax =', minmax)

print('Minimum value of A is', A.min())
print('So we add k =', abs(A.min()) + 1, 'and get new matrix A:')
A = A+(abs(A.min()) + 1)
print(A)
B = np.array([1, 1, 1, 1, 1])

# find x1, x2, ... , xm
A_ub = np.array(-A.T)
b_ub = np.array(-B)
c = np.array([1, 1, 1])

res = linprog(c, A_ub, b_ub, bounds=(0, None))
print('X:', res.x)
V = 1/(sum(res.x))
p = V*res.x
print('V =', V, '\np =', p)

# find y1, y2, ... , yn
A_ub = np.array(A)
b_ub = np.array(B[:3])
c = np.array([-1, -1, -1, -1, -1])

res = linprog(c, A_ub, b_ub, bounds=(0, None))
print('Y:', res.x)
V = 1/(sum(res.x))
q = V*res.x
print('V =', V, '\nq =', q)