def find_original_set(X,Y,Z,W,V):
    return set(min(X, min(Y, min(Z, min(W, V)))))
