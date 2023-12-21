
def if_contains_anagrams(lst):
    return all(sorted(s) in map(sorted, lst[:i]) for i, s in enumerate(lst)) and len(lst) <= 18
