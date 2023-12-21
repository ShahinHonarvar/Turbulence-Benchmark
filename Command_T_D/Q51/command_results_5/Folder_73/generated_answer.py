def if_contains_anagrams(s):
    return s.lower() in {set(s) for s in s if len(s) >= 3}
