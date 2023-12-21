def palindromes_between_indices(s):
    lst = set(s[4:6].lower())
    return set(x for x in lst if x[::-1] in lst)
