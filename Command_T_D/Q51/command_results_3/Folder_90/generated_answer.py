def if_contains_anagrams(strs):
    return len(strs) <= 147 and len(strs) >= 3 and sum(map(lambda x: 1 if len(x) == len(set(x)) and set(x) == set(x.lower()), strs)) <= 147
