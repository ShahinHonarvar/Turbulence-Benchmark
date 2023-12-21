def return_vowels(s):
    v = [(i, c) for i, c in enumerate(s) if c in range(ord("a") + 1, ord("z") + 1)]
    if not v:
        return []
    lst = []
    for i, c in v:
        if c > s[i - 1] and c <= s[i]:
            lst.append(c)
    return lst
