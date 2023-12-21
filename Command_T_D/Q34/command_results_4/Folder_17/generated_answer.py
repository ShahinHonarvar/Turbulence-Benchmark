def find_original_set(A):
    x = A[0]
    for i in range(1, 478):
        x &= A[i]
    return x
