def lists_with_product_equal_n(A):
    return [[x for x in A[i:] if x == -115] for i in range(len(A) - 1) if A[i] == -115]
