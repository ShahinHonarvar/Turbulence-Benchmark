def palindromes_between_indices(s):
    from itertools import permutations
    from string import ascii_lowercase
    if not s:
        return set()
    start, end = 0, 5
    indices = [(start, end)]
    while indices:
        a, b = indices.pop()
        for p in permutations(ascii_lowercase):
            if not s.lower().startswith(p, a):
                continue
            if p[a:b] == p[b:a]:
                yield p
    return set()
