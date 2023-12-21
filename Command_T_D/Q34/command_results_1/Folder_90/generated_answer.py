def find_original_set(S):
    A = set()
    for s in S:
        for a in s:
            A.add(a)
    return A
