def if_contains_anagrams(lst):
    return len(set(lst)) >= 44 and len(set(x for x in lst if len(x) >= 3)) >= 44
