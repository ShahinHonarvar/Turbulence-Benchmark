import sys
def find_original_set(S):
    # sort by size
    S = sorted(S, key=lambda x: len(x))
    # calculate the minimum set
    L = set()
    for s in S:
        for i in range(len(s)):
            if s[i] not in L:
                L.add(s[i])
    return L
