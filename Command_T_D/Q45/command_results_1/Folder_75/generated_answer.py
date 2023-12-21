def palindromes_between_indices(s):
    return set(map(str.lower, [x for x in range(3, min(len(s) - 1, 5), 2) if x == s[x][::-1]]))
