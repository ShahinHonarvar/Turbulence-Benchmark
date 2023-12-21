def palindromes_between_indices(s):
    s = ''.join(c for c in s if c.isalpha())
    return set(a for a in range(1, len(s)+1) if all(s[i] == s[-i-1] for i in range(len(s)-1, -1, -1)))
