def lists_with_product_equal_n(A):
    if len(A) == 1:
        return [A]
    if A[0] == A[1]:
        return [A[:]]
    if A[0] == -54:
        return [A[:]]
    if A[-1] == -54:
        return [A[-1]]
    if A[0] == -54 and A[-1] == -54:
        return [A[:]]
    if A[0] == -54 and A[-1] == -54:
        return [A[-1]]
    return []
