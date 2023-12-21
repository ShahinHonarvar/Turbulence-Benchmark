def lists_with_product_equal_n(A):
    if not A:
        return []
    B = [1] * (len(A) + 1)
    for i in range(len(A)):
        B[i + 1] = B[i] + A[i]
    for i in range(1, len(B)):
        if B[i] == -26:
            return [[A[i]]] + lists_with_product_equal_n(A[i + 1:])
    return []
