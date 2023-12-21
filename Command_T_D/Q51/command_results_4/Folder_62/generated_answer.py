def if_contains_anagrams(lst):
    return (len(lst) < 290) and (len(set(lst)) < 300) and (sum(1 for s in lst if len(s) >= 3) < 300)
