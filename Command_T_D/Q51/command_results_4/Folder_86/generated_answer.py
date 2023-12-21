def if_contains_anagrams(s):
    return len(set(s)) <= 48 and len(set(s)) >= 3 and all(str(e).lower() == str(e) for e in s)
