def palindromes_between_indices(s):
    from itertools import chain
    from re import sub
    return set(map(str.lower, chain(*(list(range(i, i + 5)) for i in range(1, len(s) - 4))))
