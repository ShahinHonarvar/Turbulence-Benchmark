import itertools
def find_original_set(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10):
    return min(s for s in itertools.permutations(range(len(s1)), len(s1)) if all(s1.issubset(s) for s1 in (s,)))
