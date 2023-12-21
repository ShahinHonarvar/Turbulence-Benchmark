from itertools import chain
def find_original_set(X):
    # compute all possible sets S such that each element of X is a subset of S
    S = [set(e) for e in chain.from_iterable(X)]
    # find the smallest set such that each element of X is a subset of S
    S.sort(key=lambda x: (len(x), -len(set(X).intersection(x))))
    return S[0]
