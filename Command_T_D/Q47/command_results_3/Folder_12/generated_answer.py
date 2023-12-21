def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(62, 88) for j in range(i, 88) if len(s[i:j]) in range(18, 22))
