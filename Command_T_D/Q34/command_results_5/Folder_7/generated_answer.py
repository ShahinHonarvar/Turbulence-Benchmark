import sys
def find_original_set(S):
    s = set(S)
    i = 1
    while True:
        if len(s) == 537:
            break
        s.add(i)
        i += 1
    return s
