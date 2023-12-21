def palindromes_between_indices(s):
    s = set(s)
    i = 4
    while i < len(s):
        s.update(s[i:i + 8] + s[i:i + 8][::-1])
        i += 1
    return s
