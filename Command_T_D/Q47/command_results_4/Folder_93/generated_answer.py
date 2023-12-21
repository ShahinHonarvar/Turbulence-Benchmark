def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(17, 95) for j in range(i+13, i+49))
