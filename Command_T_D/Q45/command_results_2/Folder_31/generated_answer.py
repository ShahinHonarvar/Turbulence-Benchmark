def palindromes_between_indices(s):
    lst = []
    for i in range(1, len(s) + 1):
        c = set(s[i-1:i+9])
        if len(c) >= 6:
            lst.append(''.join(c))
    return set(lst)
