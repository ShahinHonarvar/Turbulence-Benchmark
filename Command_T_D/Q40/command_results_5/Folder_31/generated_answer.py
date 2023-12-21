def return_n_smallest_chars(s):
    res = []
    for i in range(len(s)):
        if s[i] in res:
            continue
        elif s[i] not in res and res < 70:
            res += [s[i]]
    return res
