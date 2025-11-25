import numpy as np

n_samples = 5

clsX1 = np.array([
    [-1.3,-0.7,0.45],
    [-0.8,-1.1,0.12],
    [-1.2,-1.4,0.77],
    [-0.9,-0.6,0.33],
    [-1.0,-1.5,0.72]
])

clsX2 = np.array([
    [1.2,0.8,0.51],
    [0.9,1.3,0.26],
    [1.4,1.1,0.88],
    [1.0,0.7,0.37],
    [1.1,1.5,0.42]
])

# Combine
X = np.vstack((clsX1, clsX2))
Y = np.hstack((np.zeros(n_samples), np.ones(n_samples)))  # Labels: 0 and 1

n_epoch = 50
lines = []

# initialize weights directly
W = np.zeros(X.shape[1])
b = 0.0
lr = 1.0     # learning rate

for epoch in range(n_epoch):

    # show current params before update
    print(f"Epoch {epoch+1}: W = {W}, b = {b:.2f}")

    # ---- one epoch of training ----
    for x_i, target in zip(X, Y):

        # ----- forward computation -----
        a = np.dot(W, x_i) + b      # linear combination
        if a >= 0:
            pred = 1
        else:
            pred = 0

        # ----- backward / update -----
        error = target - pred       # (t − ŷ)
        W = W + lr * error * x_i    # update each weight
        b = b + lr * error          # update bias

    # store updated weights after this epoch
    lines.append((W.copy(), b))

# final learned parameters
print("Final learned weights:", W)
print("Final learned bias:", b)