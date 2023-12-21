import sys
def find_original_set(X):
    sys.setrecursionlimit(10**5)
    X = set(X)
    A = set()
    for i in range(1, 10**5+1):
        if X & {i} == X:
            A.add(i)
            if len(A) == len(X):
                break
    return A
