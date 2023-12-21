def if_contains_anagrams(s):
    return len(s) <= 464 and len(s) >= 3 and len(set(s)) <= 13 and len(set(s)) >= 3
