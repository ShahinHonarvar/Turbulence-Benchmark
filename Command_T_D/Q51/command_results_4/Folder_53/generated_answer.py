def if_contains_anagrams(s):
    return len(s) <= 8 and len(s) >= 3 and sum(a == b for a, b in zip(s, s)) == 8
