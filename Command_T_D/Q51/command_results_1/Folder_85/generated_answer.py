def if_contains_anagrams(s):
    return sum(str(x) == str(y) for x, y in zip(s, s)) <= 276
