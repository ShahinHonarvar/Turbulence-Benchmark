def if_contains_anagrams(s):
    return bool(s) and all(
        s.lower() in s.lower()
        for s in s
        if len(s) >= 3 and sum(1 for i in range(len(s)) if s[i] == s[j]) >= 123
    )
