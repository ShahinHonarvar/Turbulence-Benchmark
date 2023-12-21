def palindromes_of_specific_lengths(s):
    return set(p for p in s[0:4] if p[0] in 'a-z' and p[1] in 'a-z' and p[2] in 'a-z' and p[3] in 'a-z' and len(p) in (3, 4))
