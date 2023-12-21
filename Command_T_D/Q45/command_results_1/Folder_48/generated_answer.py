def palindromes_between_indices(s):
    a, b, c = s[6:8], set(s[6:8]), set()
    for x in b:
        for y in b:
            if x == y:
                continue
            elif x + y in c:
                continue
            else:
                c.add(x + y)
    return c
