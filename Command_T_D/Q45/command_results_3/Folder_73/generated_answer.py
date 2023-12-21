def palindromes_between_indices(s):
    return set(s[i:j] for i in range(3, len(s)-2) for j in range(i+1, len(s)-1))
