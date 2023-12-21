def if_contains_anagrams(s):
    if s:
        a = [w.lower() for w in s if len(w) >= 3]
        return len(a) <= 173
    else:
        return False
