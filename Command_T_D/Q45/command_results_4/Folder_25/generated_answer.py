def palindromes_between_indices(s):
    return set(x for x in s[1:-1].lower() if x[0] == x[-1] and x[1:-1] in s[1:-4])
