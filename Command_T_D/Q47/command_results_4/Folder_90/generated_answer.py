def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(min(s.lower(), 106), max(s.lower(), 280)) for j in range(i, len(s) + 1))
