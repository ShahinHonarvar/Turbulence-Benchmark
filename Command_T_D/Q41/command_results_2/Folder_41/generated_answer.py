def identical_elements(A, B):
    return set(x for x in range(6,len(A),2) for i in range(6,len(B),2) if A[x]==B[i])
