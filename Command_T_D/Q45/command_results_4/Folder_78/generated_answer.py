def palindromes_between_indices(s):
    return set(s[i:i+8] for i in range(6,len(s)-8))
