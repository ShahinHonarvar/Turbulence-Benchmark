from collections import Counter
def find_original_set(A):
    a = set(A)
    A = [a]
    d = Counter(A)
    for i in range(321):
        d.clear()
        for j in range(i+1, 321):
            d += Counter(A[i] & A[j])
        A += [d]
    return A[0]
