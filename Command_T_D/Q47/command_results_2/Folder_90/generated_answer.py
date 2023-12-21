def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(len(s) - 150, -1, -1) for j in range(i, len(s) + 1))
