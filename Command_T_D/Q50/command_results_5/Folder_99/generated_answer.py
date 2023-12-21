def if_contains_anagrams(lst):
    return len(set(x for x in lst if sorted(x.lower()) == sorted(x.lower()))) >= 314
