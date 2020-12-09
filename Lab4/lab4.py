# 10) V(l) =100; V(2) = 180; V(3) = 120; V(l, 2) = 300; V(l, 3) = 250; V(2, 3) = 340; V(1, 2, 3) = 480.

# 1. Перевірити виконання умов супераддитивності й істотності для даної кооперативної гри.
# 2. Виразити значення характеристичної функції в 0-1 спрощеній формі.
# 3. Перевірити умови, що визначають непорожнечу С-ядра і знайти один з варіантів розв’язку гри (поділ X).
# 4. Визначити розв’язки кожного з гравців у разі їх об’єднання на основі використання вектора Шеплі. Перевірити належність вектора Шеплі С-ядру.
from fractions import Fraction
from math import factorial

V = {}
V['1'] = 100
V['2'] = 180
V['3'] = 120
V['1,2'] = 300
V['1,3'] = 250
V['2,3'] = 340
V['1,2,3'] = 480
N = {'1', '2', '3'}

# 1. Перевірити виконання умов супераддитивності й істотності для даної кооперативної гри.
superadditive = True
total = 0
for i in range(1, 4):
    total += V[str(i)]
    if V[str(i)] + V[','.join(sorted(N-{str(i)}))] >= V[','.join(sorted(N))]:
        superadditive = False

if superadditive:
    print("The characteristic function is superadditive")
else:
    print('The characteristic function is not superadditive')

if total < V[','.join(sorted(N))]:
    print('The game is essential')
else:
    print('The game is not essential')

# 2. Виразити значення характеристичної функції в 0-1 спрощеній формі.
_V = {}
_V['1'] = 0
_V['2'] = 0
_V['3'] = 0
_V['1,2'] = Fraction(V['1,2']-(V['1']+V['2']), V['1,2,3']-(V['1']+V['2']+V['3']))
_V['1,3'] = Fraction(V['1,3']-(V['1']+V['3']), V['1,2,3']-(V['1']+V['2']+V['3']))
_V['2,3'] = Fraction(V['2,3']-(V['2']+V['3']), V['1,2,3']-(V['1']+V['2']+V['3']))
_V['1,2,3'] = 1
print("V`:", _V)

# 3. Перевірити умови, що визначають непорожнечу С-ядра і знайти один з варіантів розв’язку гри (поділ X).
empty = False
for i in range(1, 4):
    if _V[str(i)] > Fraction(1, 3):
        empty = True
for i in ['1,2', '1,3', '2,3']:
    if _V[i] > Fraction(1, 2):
        print(_V[i])
        empty = True
if _V['1,2,3'] != 1:
    empty = True
print('The C-core of the system is not empty') if not empty else print('The C-core of the system is empty')

_X = (0.3, 0.3, 0.4)
for i in range(1, 4):
    if _V[str(i)] >= _X[i - 1]:
        print('Error')
if _V['1,2'] >= _X[0] + _X[1] or _V['1,3'] >= _X[0] + _X[2] or _V['2,3'] >= _X[1] + _X[2]:
    print('Error')
if _V['1,2,3'] != _X[0] + _X[1] + _X[2]:
    print('Error')
print('X` =', _X)

_k = V['1,2,3'] - (V['1'] + V['2'] + V['3'])
print(_k)
X = []
for i in range(1, 4):
    X.append(_k*_X[i - 1] + V[str(i)])
print('X =', X, 'sum =', sum(X))

# 4. Визначити розв’язки кожного з гравців у разі їх об’єднання на основі використання вектора Шеплі. Перевірити належність вектора Шеплі С-ядру.
f = []
f.append(Fraction(factorial(3-1)*factorial(3-3), factorial(3))*(V['1,2,3']-V['2,3']) + \
    Fraction(factorial(2-1)*factorial(3-2),factorial(3))*(V['1,2']-V['2']) + \
    Fraction(factorial(2-1)*factorial(3-2), factorial(3))*(V['1,3']-V['3']) + \
    Fraction(factorial(1-1)*factorial(3-1), factorial(3))*(V['1']-0))

f.append(Fraction(factorial(3-1)*factorial(3-3), factorial(3))*(V['1,2,3']-V['1,3']) + \
    Fraction(factorial(2-1)*factorial(3-2),factorial(3))*(V['1,2']-V['1']) + \
    Fraction(factorial(2-1)*factorial(3-2), factorial(3))*(V['2,3']-V['3']) + \
    Fraction(factorial(1-1)*factorial(3-1), factorial(3))*(V['2']-0))

f.append(Fraction(factorial(3-1)*factorial(3-3), factorial(3))*(V['1,2,3']-V['1,2']) + \
    Fraction(factorial(2-1)*factorial(3-2),factorial(3))*(V['1,3']-V['1']) + \
    Fraction(factorial(2-1)*factorial(3-2), factorial(3))*(V['2,3']-V['2']) + \
    Fraction(factorial(1-1)*factorial(3-1), factorial(3))*(V['3']-0))

shapley_belongs = True
for i in range(1, 4):
    if V[str(i)] > f[i - 1]:
        shapley_belongs = False
if V['1,2'] > f[0] + f[1] or V['1,3'] > f[0] + f[2] or V['2,3'] > f[1] + f[2]:
    shapley_belongs = False
if V['1,2,3'] != f[0] + f[1] + f[2]:
    shapley_belongs = False

print('Shapley value belongs to C-core') if shapley_belongs else print('Shapley value not belongs to C-core')
print('Shapley value is', f, 'sum =', sum(f))
