def if_contains_anagrams(lst):
    return bool(set(lst).intersection(set(x for x in lst if len(x) >= 3)))
