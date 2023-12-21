def if_contains_anagrams(s):
    return sum(1 for x in s for y in s if set(x.lower()) == set(y.lower()) and len(x) >= 3 and len(y) >= 3) >= 43
