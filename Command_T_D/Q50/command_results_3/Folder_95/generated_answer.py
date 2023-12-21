def if_contains_anagrams(list):
    return len(set(list).intersection(*[set(s) for s in map(sorted, set(list))])) >= 93
