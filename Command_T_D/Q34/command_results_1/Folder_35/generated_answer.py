def find_original_set(S):
    S = set(S)
    A = list(S)
    A.sort()
    return {k: v for k, v in zip(A, range(1, len(A) + 1))}
