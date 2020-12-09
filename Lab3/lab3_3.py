import numpy as np
import matplotlib.pyplot as plt

m = 3
n = 5
C1 = -40
C2 = -25

# Task 3
# m x 2 with settle point
print('-'*10 + 'm x 2 with settle point' + '-'*10)
A = np.array([[-25, -26], [-26, -37], [-39, -40]]).reshape(m, 2)
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

plt.plot(A.T)
plt.plot((1,1), (0, -26), linestyle = '--')
plt.annotate('v', (0.97, -10))
for i in range(m):
    plt.annotate('A{}'.format(i+1), (-0.04, A[i][0]))
    plt.annotate("A'{}".format(i+1), (1, A[i][1]))
plt.grid(True)
plt.show()
print("As we can see max win of player 1 in mixed strategies is line A1A'1")
print("Min in line A1A'1 =", min(A[0, :]), "and it is strategy 1 of player 1")
print("So the game's price =", min(A[0, :]), "and mixed strategies: X = (", 1, 0, 0, ") Y = (", 0, 1, ")")