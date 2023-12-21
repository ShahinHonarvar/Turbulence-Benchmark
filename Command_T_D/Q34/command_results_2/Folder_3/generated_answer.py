import sys
def find_original_set(S):
    A = set(S)
    C = set(sum(S, []))
    M = set(C | A)
    D = set(M | C)
    X = set(D | C)
    return X
