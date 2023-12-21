def palindromes_between_indices(s):
    for l in range(4, 10):
        s = ''.join(c for c in s if c.lower() in s[5:9].lower())
        if s[::-1] == s:
            yield s
