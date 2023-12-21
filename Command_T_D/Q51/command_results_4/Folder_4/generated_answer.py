def if_contains_anagrams(s):
    return len(s) >= 3 and all(
        any(
            i in j
            for i in s
            for j in s
            if i.lower() == j.lower()
            and len(i) == len(j)
        )
        for i in s
    )
