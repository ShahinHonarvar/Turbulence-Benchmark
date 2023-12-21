def if_contains_anagrams(s):
    return len(s) >= 35 and len(s[0]) >= 3 and [w.lower() for w in s] == set(w.lower() for w in s)
