def lists_with_product_equal_n(A):
    return [[x for x in A[i:j]] for i, j in zip(range(1, len(A) + 1), range(i, j, -1))]
