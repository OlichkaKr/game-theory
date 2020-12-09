import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

m = 3
n = 5
C1 = -40
C2 = -25

# Task 4
# m x 2 without settle point
print('-'*10 + 'm x 2 without settle point' + '-'*10)
A = np.array([[-30, -26], [-25, -37], [-32, -40]]).reshape(m, 2)
print(A)

maxmin = max(A.min(axis=1))
minmax = min(A.max(axis=0))

print('Maxmin =', maxmin)
print('Minmax =', minmax)

plt.plot(A.T)
plt.plot((0.31, 0.31), (0, -28.7), linestyle = '--')
plt.annotate('N', (0.31, -30))
for i in range(m):
    plt.annotate('A{}'.format(i+1), (-0.04, A[i][0]))
    plt.annotate("A'{}".format(i+1), (1, A[i][1]))
plt.grid(True)
plt.show()
print("As we can see max win of player 1 in mixed strategies is curve A2NA'1")
print("Find an intersection of A2A'2 and A1A'1:")
print("-30x-25(1-x)=v")
print("-26x-37(1-x)=v")
# -30x+25x+26x-37x=25-37
x = Fraction(25-37, -30+25+26-37)
v = -30*x-25*(1-x)
print("x =", x)
print("v =", v)
print("-30y-26(1-y)=v")
print("-25-37(1-y)=v")
y = Fraction(v+26, -30+26)
print("y =", y)

print("So the  game's price =", v, "and mixed strategies: X = (", x, 1-x, 0, ") Y = (", y, 1-y, ")")