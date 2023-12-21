from itertools import combinations
def find_original_set(X):
    return {*min( combinations(X, 2), key=lambda x: len(x)), **X}
