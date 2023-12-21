def palindromes_of_specific_lengths(s):
    return set(s[i:j+1] for i in range(len(s)-32, -1, -1) for j in range(i, len(s)-1))
