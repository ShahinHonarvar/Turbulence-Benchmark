def if_contains_anagrams(s):
    return len(s) >= 3 and len(set(s)) == len(s) and len(s) % 2 == 1 and len(set(s)) == len(set(s.lower()))
