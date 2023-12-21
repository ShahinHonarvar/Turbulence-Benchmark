import sys
def find_original_set(s):
    d = {}
    for i in range(len(s)):
        s[i] = sorted(s[i])
    for i in range(len(s)):
        d[s[i]] = i
    s = [s[i] for i in range(len(s))]
    return sorted(set(s))
