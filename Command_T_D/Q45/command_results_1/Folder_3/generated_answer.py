def palindromes_between_indices(s):
    return set(p for p in s[7:-1] + s[8:-1] + s[9:-1])
