import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from sklearn.datasets import load_svmlight_file


# zad1
X, y = load_svmlight_file('breast-cancer')

y = np.array(y)
fun = lambda x : -1 if x == 2 else 1
yfun = np.vectorize(fun)
y = yfun(y)
print(y)


np_X = np.array(X.toarray())

def normalize_column(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))

def normalize(x):
    return np.apply_along_axis(normalize_column, axis=0, arr=x)

X = normalize(np_X)
print(X)


# zad2
firstDimention = []
secondDimention = []
for x in X:
    firstDimention.append(x[0])
    secondDimention.append(x[1])

colors = []
for value in y:
    if value == -1:
        colors.append('red')
    else:
        colors.append('green')


plt.scatter(firstDimention, secondDimention, c = colors)
# plt.scatter(X[0], X[1], c = ['red', 'green'])
plt.show()

# zad3

beta_regression = np.dot(np.dot(inv(np.dot(np_X.T, np_X)), np_X.T), y)
print(beta_regression)