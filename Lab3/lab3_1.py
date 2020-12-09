import numpy as np
import matplotlib.pyplot as plt

m = 3
n = 5
C1 = -40
C2 = -25

# Task 1
# 2 x n with settle point
print('-'*10 + '2 x n with settle point' + '-'*10)
A = np.array([[-30, -25, -37, -28, -33], [-36, -37, -40, -26, -32]]).reshape(2, n)
print(A)

maxmin = max(A.min(axis=1))
minmax = min(A.max(axis=0))

print('Maxmin =', maxmin)
print('Minmax =', minmax)

xy = np.where(A == maxmin)
settle = list(zip(*xy))

for i in settle:
    if A[i] == max(A[:,i[1]]):
        print('Settle point is (i0 = {}, j0 = {})'.format(i[0] + 1, i[1] + 1))


plt.plot(A)
plt.plot((0,0), (0, -37), linestyle = '--')
plt.annotate('v', (-0.03, -10))
for i in range(n):
    plt.annotate('B{}'.format(i+1), (-0.04, A[0][i]))
    plt.annotate("B'{}".format(i+1), (1, A[1][i]))
plt.grid(True)
plt.show()
print("As we can see min win of player 1 in mixed strategies is line B3B'3")
print("Max in line B3B'3 =", max(A[:, 2]), "and it is strategy 1 of player 1")
print("So the game's price =", max(A[:, 2]), "and mixed strategies: X = (", 1, 0, ") Y = (", 0, 0, 1, 0, 0, ")")