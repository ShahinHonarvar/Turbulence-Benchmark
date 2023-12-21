
def if_contains_anagrams(lst):
    pairs = 0
    for s1 in lst:
        for s2 in lst[lst.index(s1) + 1:]:
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                pairs += 1
    return pairs >= 29
