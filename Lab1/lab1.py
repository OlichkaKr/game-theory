# var 10
import numpy as np

class Game:
    m = 3
    n = 5
    C1 = -4
    C2 = 5

    def __init__(self, matrix):
        self.G = np.array(matrix).reshape(self.m, self.n)
    
    def print_matrix(self):
        print(self.G)

    def find_settle_point(self):
        self._maxmin = self.find_maxmin()
        self._minmax = self.find_minmax()
        if self._maxmin != self._minmax:
            return None
        else:
            xy = np.where(self.G == self._maxmin)
            return list(zip(*xy))

    def print_optimal_strategy(self):
        self._settle = self.find_settle_point()
        if not self._settle:
            print('No settle point')
        else:
            for i in self._settle:
                if self.G[i] == max(self.G[:,i[1]]):
                    print('Settle point is (i0 = {}, j0 = {})'.format(i[0], i[1]))

    def find_maxmin(self):
        return max(self.G.min(axis=1))

    def find_minmax(self):
        return min(self.G.max(axis=0))

def print_result(game):
    game.print_matrix()
    print('Settle point: {}'.format(game.find_settle_point()))
    game.print_optimal_strategy()
    print('Maxmin: ', game.find_maxmin())
    print('Minmax: ', game.find_minmax())

# більше 1 сідлової точки
print('-'*20)
g1 = Game([[-2, 0, -1, -2, 1], [-3, 5, 0, 2, -3], [-2, 5, 4, -1, -3]])
print_result(g1)

print('-'*20)
g2 = Game([[0, 2, -3, -1, 1], [0, 3, 4, 5, 0], [-4, 3, -3, 1, 5]])
print_result(g2)

# одна сідлова точка
print('-'*20)
g3 = Game([[5, 4, 3, 1, 3], [1, 0, -3, 0, 4], [1, 1, 2, 0, -4]])
print_result(g3)

print('-'*20)
g4 = Game([[-1, 0, 2, 0, -1], [4, 5, -3, 5, -4], [2, -2, 3, 2, -3]])
print_result(g4)

# нема сідлової точки
print('-'*20)
g5 = Game([[1, -2, -2, 1, 3], [4, -4, -1, -4, -3], [4, 3, 2, 4, -4]])
print_result(g5)

print('-'*20)
g6 = Game([[-1, 5, 4, 1, -2], [-4, 4, -3, 3, 4], [1, -3, 3, 1, 4]])
print_result(g6)