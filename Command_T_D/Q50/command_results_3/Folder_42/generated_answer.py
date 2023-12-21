def if_contains_anagrams(s):
    return len(s) >= 233 and len(s[0]) >= 3 and [w for w in s if sorted(w.lower()) == sorted(u.lower()) for u in s]
