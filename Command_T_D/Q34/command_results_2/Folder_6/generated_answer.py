def find_original_set(S):
    return min(set(range(min(S), max(S) + 1)), key=lambda x: len(S) == 1 or S[0] == set(x))
