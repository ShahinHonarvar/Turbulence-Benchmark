def palindromes_between_indices(s):
    s = s.lower()
    return set(x for x in range(3, len(s) - 5, 2) if s[x:x + 5] == s[x:x + 5][::-1])
