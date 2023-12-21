def find_original_set(S):
    return set(S).union(set(sum(S, [])))
