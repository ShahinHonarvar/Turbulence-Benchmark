def find_original_set(S):
    A = set(S)
    C = set()
    for i in range(1, len(A)):
        if A.intersection(C):
            C = A
        else:
            C.add(A)
    return C
