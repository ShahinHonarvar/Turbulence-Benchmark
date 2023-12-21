def identical_elements(A, B):
    return set(a for a in range(len(A)) if A[a] in B)
