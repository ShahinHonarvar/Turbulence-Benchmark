def if_contains_anagrams(s):
    return len(s) > 140 and len(s) % 2 == 0 and len(set(s)) == len(s)
