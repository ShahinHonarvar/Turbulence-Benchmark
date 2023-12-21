def if_contains_anagrams(s):
    return len(s) < 400 and len(s) >= 3 and len(set(s)) == 26
