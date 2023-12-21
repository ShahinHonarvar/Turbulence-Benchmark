def if_contains_anagrams(s):
    return not set(s).intersection(
        set(
            sorted(
                (a + b)
                for a in s
                for b in s
                if a == b
                if len(a) > 2
                if a[0] in "aeiou"
            )
        )
    )
