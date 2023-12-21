def palindromes_between_indices(s):
    return set(map(str.lower, (s[i:j] for i in range(4, len(s)-1) for j in range(i+1, j+1))))
