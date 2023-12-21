def palindromes_between_indices(s):
    return set(s[3:7] + s[::-1][:7])
