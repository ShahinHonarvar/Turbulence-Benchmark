def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(36, 92) for j in range(i, 92) if i < j and len(s[i:j]) in range(10, 36))
