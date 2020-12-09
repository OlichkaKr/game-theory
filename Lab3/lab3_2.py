import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

m = 3
n = 5
C1 = -40
C2 = -25

# Task 2
# 2 x n without settle point
print('-'*10 + '2 x n without settle point' + '-'*10)
A = np.array([[-30, -25, -27, -36, -31], [-40, -36, -35, -33, -37]]).reshape(2, n)
print(A)

maxmin = max(A.min(axis=1))
minmax = min(A.max(axis=0))

print('Maxmin =', maxmin)
print('Minmax =', minmax)

plt.plot(A)
plt.plot((0.46, 0.46), (0, -34.8), linestyle = '--')
plt.annotate('N', (0.45, -36))
for i in range(n):
    plt.annotate('B{}'.format(i+1), (-0.04, A[0][i]))
    plt.annotate("B'{}".format(i+1), (1, A[1][i]))
plt.grid(True)
# plt.show()
print("As we can see min win of player 1 in mixed strategies is curve B4NB'1")
print("Find an intersection of B4B'4 and B1B'1:")
print("-30x-40(1-x)=v")
print("-36x-33(1-x)=v")
# -30*x+40*x+36*x-33*x=40-33
x = Fraction(40-33, -30+40+36-33)
v = -30*x-40*(1-x)
print("x =", x)
print("v =", v)
print("-30y-36(1-y)=v")
print("-40y-33(1-y)=v")
y = Fraction(v+36, -30+36)
print("y =", y)

print("So the  game's price =", v, "and mixed strategies: X = (", x, 1-x, ") Y = (", y, 0, 0, 1-y, 0, ")")