def if_contains_anagrams(lst):
    return not (any(a.lower() == b.lower() for a, b in zip(lst, lst[1:]) if all(x != y for x, y in zip(a, b)) and len(a) >= 3))
