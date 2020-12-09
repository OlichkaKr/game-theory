import numpy as np
import matplotlib.pyplot as plt

m = 3
n = 5
C1 = -4
C2 = 5
N = 10
v = []
p_new = [0]*m
q_new = [0]*n

G = np.array([[1, 4, 2, 3, 0], [2, 3, -3, 4,  1], [3, -4, 0, 1, 2]]).reshape(m, n)
print(G)

maxmin = max(G.min(axis=1))
minmax = min(G.max(axis=0))

print('Maxmin =', maxmin)
print('Minmax =', minmax)

# step 1
i1 = 1
j1 = 2
p1 = [1, 0, 0]
q1 = [1, 0, 0, 0, 0]
p_new = p1.copy()
q_new = q1.copy()

# step N
for i in range(2, N+1):
    sum_iq = [sum(G[row,:]*q_new) for row in range(G.shape[0])]
    a_n = max(sum_iq)
    i_new = sum_iq.index(max(sum_iq))

    sum_jp = [sum(G[:,col]*p_new) for col in range(G.shape[1])]
    b_n = min(sum_jp)
    j_new = sum_jp.index(min(sum_jp))

    for idx in range(m):
        p_new[idx] = ((i-1) * p_new[idx])/((i-1) + 1) if idx != i_new else ((i-1) * p_new[idx] + 1)/((i-1) + 1)
    for idx in range(n):
        q_new[idx] = ((i-1) * q_new[idx])/((i-1) + 1) if idx != j_new else ((i-1) * q_new[idx] + 1)/((i-1) + 1)
    
    print('-'*20)
    print('a{} = {}'.format(i-1, a_n))
    print('b{} = {}'.format(i-1, b_n))
    print('i{} = {}'.format(i, i_new + 1))
    print('j{} = {}'.format(i, j_new + 1))
    print('p{}: {}, sum={}'.format(i, p_new, sum(p_new)))
    print('q{}: {}, sum={}'.format(i, q_new, sum(q_new)))

    v.append((a_n + b_n)/2)

# vvvvv = [2, 2.25, 1.833, 1.875, 2.133, 2.291, 2.257, 2.02, 1.98, 1.875, 1.984, 2.208]
print(v)
plt.plot(v)
plt.show()