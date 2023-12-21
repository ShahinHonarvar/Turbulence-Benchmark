import sys
def find_original_set(S):
    A = set()
    for s in S:
        A.update(s)
    return A
