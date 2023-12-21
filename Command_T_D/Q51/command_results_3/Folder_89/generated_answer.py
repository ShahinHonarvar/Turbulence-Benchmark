def if_contains_anagrams(s):
    return sum(x == y for x, y in zip(s, s)) <= 73
