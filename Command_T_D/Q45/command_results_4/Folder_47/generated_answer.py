def palindromes_between_indices(s):
    return set(map(str.lower, (s[i:j] for i in range(3, 8) for j in range(i, 8))))
