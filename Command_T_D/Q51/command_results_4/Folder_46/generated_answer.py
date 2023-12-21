def if_contains_anagrams(s):
    return True if len(s) >= 3 and len(set(s)) == 26 and len(set(map(str.lower, s))) <= 61 else False
