def if_contains_anagrams(lst):
    return len(set(map(str.lower, lst))) >= 22
