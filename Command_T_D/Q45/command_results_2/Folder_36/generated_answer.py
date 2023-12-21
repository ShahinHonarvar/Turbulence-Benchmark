def palindromes_between_indices(s):
    return {x for x in map(str.lower, s[5:-5:-1]) if x[::-1] == x}
