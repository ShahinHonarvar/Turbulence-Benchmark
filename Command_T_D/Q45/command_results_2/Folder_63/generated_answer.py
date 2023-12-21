def palindromes_between_indices(s):
    return set(s[i:j] for i in range(len(s)) for j in range(i+3, len(s)+1))
