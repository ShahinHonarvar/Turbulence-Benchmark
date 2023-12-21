import itertools
def find_original_set(A, B, C, D, E):
    sets = set(range(len(A)))
    for s in itertools.permutations(sets):
        if all(set(A).issubset(s) and set(B).issubset(s) and set(C).issubset(s) and set(D).issubset(s) and set(E).issubset(s)):
            return s
    return None
