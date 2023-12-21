def if_contains_anagrams(s):
    return len(s) >= 43 and sum(
        1
        for x in s
        for y in s
        if len(x) >= 3 and len(y) >= 3 and sorted(x.lower()) == sorted(y.lower())
    )
