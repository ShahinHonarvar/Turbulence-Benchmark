def if_contains_anagrams(s):
    return len(s) > 1 and len(s[0]) > 2 and len(s[1]) > 2 and len(s) == len(set(s)) and all(
        s[0] == s[i].lower()
        for i in range(len(s))
    )
