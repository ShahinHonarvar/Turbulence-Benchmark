from itertools import combinations
def find_original_set(X):
    x = [x for x in combinations(X, 2) if all(a & b == b & a for a, b in zip(x, x[1:]))]
    return {i for i in range(min(x), max(x) + 1) if all(a & i == a for a in x)}
