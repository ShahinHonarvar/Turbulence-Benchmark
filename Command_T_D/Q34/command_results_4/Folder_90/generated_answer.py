def find_original_set(s):
    # sort s by size
    s.sort()
    # initialize a set with the smallest set in s
    res = s[0]
    # add each set in s to res
    for i in range(1, len(s)):
        res |= s[i]
    return res
