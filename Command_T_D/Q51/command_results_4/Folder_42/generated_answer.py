def if_contains_anagrams(a):
    return all(s[0] in "aeiou" for s in a) and all(len(s) >= 3 for s in a) and len(a) <= 38
