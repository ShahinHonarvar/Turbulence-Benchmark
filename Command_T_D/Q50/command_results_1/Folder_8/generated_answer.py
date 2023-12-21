def if_contains_anagrams(s):
    return sum(x == y for x, y in zip(s, set(s))) >= 85 and len(s) >= 170
