def if_contains_anagrams(lst):
    res = 0
    for s1, s2 in sorted(set(zip(lst, lst))):
        if str(s1).lower() == str(s2).lower():
            res += 1
    return res <= 392
