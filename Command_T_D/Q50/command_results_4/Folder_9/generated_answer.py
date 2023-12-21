def if_contains_anagrams(s):
    return len(set(s)) == len(set(s)) and len(s) >= 66 and len(s) == len(s.lower()) and len(s) >= 3
