def find_original_set(S):
    return min(set(range(min(S), max(S) + 1)), key=lambda x: set(S).issubset(set(x)))
