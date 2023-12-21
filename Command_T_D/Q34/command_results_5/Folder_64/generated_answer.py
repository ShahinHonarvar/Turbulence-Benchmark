def find_original_set(A, B, C, D, E, F):
    return min(set(A + B + C + D + E + F), key=lambda x: len(x))
