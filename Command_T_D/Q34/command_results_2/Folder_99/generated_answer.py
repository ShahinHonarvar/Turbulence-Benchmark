import sys
def find_original_set(S):
    s = set(S)
    i = 1
    while i < len(S):
        if S[i] not in s:
            s.add(S[i])
            i += 1
        else:
            s.remove(S[i])
            i += 1
        s = list(s)
        s.sort()
        s = s[:-1]
        S = [s]
        i += 1
    return S
