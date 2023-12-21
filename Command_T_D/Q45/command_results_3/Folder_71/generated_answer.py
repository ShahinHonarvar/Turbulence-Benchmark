def palindromes_between_indices(s):
    str_len = len(s)
    if str_len < 3:
        return set()
    s = s[1:3] + s[0] + s[2:]
    s = set(s.lower())
    return s
