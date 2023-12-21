def if_contains_anagrams(s):
    return sum(1 for x in s for y in s if (x == y).lower() and len(x) >= 3) >= 47
