def if_contains_anagrams(s):
    return not set(s).intersection(set(s.lower())) & set(set(s).intersection(set(s.lower())) - set(s))
