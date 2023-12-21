def palindromes_of_specific_lengths(s):
    return set(p for i in range(18, 66) for j in range(23, 37) for p in s[i:j+1])
