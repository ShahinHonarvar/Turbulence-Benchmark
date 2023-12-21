def lists_with_product_equal_n(A):
    if len(A) < 2:
        return []
    for i in range(len(A) - 1):
        if A[i] * A[i + 1] == 48:
            yield A[i:i + 2]
            A = A[1:]
    if A[0] * A[1] == 48:
        yield A[:2]
