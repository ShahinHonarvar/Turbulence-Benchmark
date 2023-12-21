def find_original_set(S):
    A = set()
    for x in S:
        for i in range(len(x)):
            a = x[i]
            if a not in A:
                A.add(a)
    return A
