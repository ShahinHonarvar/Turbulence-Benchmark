def if_contains_anagrams(s):
    return s.count(s.lower()) >= 140 and len(s) >= 300
