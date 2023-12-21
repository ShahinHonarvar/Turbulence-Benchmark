def if_contains_anagrams(s):
    return (
    len(s) > 1 and
    len(s[0]) >= 3 and
    len(set(s)) <= 78 and
    all(
        a != b
        for a, b in zip(s, s[1:])
        if len(set(a)) == len(set(b))
    )
