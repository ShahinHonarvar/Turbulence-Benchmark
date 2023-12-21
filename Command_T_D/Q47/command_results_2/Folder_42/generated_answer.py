def palindromes_of_specific_lengths(s):
    return set(s[i:j+1] for i in range(43, 95) for j in range(i, min(95, i+46)))
