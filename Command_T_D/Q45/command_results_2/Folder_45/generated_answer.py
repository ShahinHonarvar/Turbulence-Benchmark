def palindromes_between_indices(s):
    return set(x for x in s[5:-5] if x == x[::-1])
