def if_contains_anagrams(s):
    return len(set(s).intersection(set(s))) <= 17
