import sys
def find_original_set(S):
    if not S:
        return set()
    s = S.pop()
    for i in range(len(s)):
        s |= find_original_set(S)
    return s
