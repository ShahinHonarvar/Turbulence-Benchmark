def lists_with_product_equal_n(A):
    return [[i for i in A[s:t+1]] for s,t in zip(A,A[1:]+[A[0]]) if 1*(s or -1)*(t+1 or -1) == -6]
