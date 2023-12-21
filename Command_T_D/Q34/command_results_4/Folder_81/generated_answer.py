import sys
def find_original_set(S):
    s = set(S)
    return min(s for s in range(1, len(s) + 1) if all(s == s1 for s1 in S))
