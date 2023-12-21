def if_contains_anagrams(s):
    return len(s) <= 92 and len(s) >= 3 and all(
        set(str(a)) == set(str(b))
        for a, b in zip(s, s[1:])
        if a == b.lower()
    )
