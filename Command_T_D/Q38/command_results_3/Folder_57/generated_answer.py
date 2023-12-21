import sys
def find_subset_of_length_n(s):
    if not s:
        return 1
    m = 1
    x = 1
    for i in range(len(s)):
        if i < n:
            m = m * x
        else:
            break
        x = x * (len(s)-i-1)
    return m
