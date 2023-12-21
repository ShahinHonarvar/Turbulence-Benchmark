import sys
def find_original_set(S):
    s = set()
    for i in S:
        for j in i:
            s.add(j)
    return s
