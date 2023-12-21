import sys
def find_original_set(s):
    m = max(s, key=len)
    s = set(range(max(s) + 1))
    for a in s:
        for b in range(a + 1, m + 1):
            if all(x in range(b, a) for x in s):
                s.add(b)
    return s
