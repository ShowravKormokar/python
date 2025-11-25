import numpy as np

n_samples = 10

X_class1 = np.array([
    [-1.3, -0.7],
    [-0.8, -1.1],
    [-1.2, -1.4],
    [-0.9, -0.6],
    [-1.5, -1.2],
    [-0.7, -1.3],
    [-1.1, -0.8],
    [-1.4, -1.0],
    [-0.6, -0.9],
    [-1.0, -1.5]
])

X_class2 = np.array([
    [1.2, 0.8],
    [0.9, 1.3],
    [1.4, 1.1],
    [1.0, 0.7],
    [1.5, 1.2],
    [0.8, 1.4],
    [1.3, 0.9],
    [1.1, 1.5],
    [0.7, 1.0],
    [1.6, 1.3]
])
X = np.vstack((X_class1, X_class2))
y = np.hstack((np.zeros(n_samples), np.ones(n_samples)))  # Labels: 0 and 1
print(zip(X, y))