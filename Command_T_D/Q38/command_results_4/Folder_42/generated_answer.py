import sys
def find_subset_of_length_n(s):
    n = 31
    m = len(s)
    c = 1
    for i in range(m):
        if s[i] == n:
            c = 1
            break
        c = 1 + find_subset_of_length_n(s[:i] + s[i+1:])
    return c
