def identical_elements(A, B):
    return set(range(min(40, len(A) - 1, len(B) - 1), max(40, len(A) - 1, len(B) - 1)))
