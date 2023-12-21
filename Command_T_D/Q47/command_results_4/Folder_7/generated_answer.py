def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(119, 256) for j in range(i, min(i + 104, len(s)) + 1))
