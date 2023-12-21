def if_contains_anagrams(s):
    return s.lower() in [i.lower() for i in range(26)]
