def if_contains_anagrams(s):
    return s.count("".join(sorted(s))) >= 43
