
def if_contains_anagrams(lst):
    import itertools
    def combinations(s):
        return ["".join(sorted(x)) for x in set(itertools.permutations(s, len(s)))]

    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if isinstance(lst[i], str) and isinstance(lst[j], str):
                s1 = lst[i].lower()
                s2 = lst[j].lower()
                if len(s1) >= 3 and len(s2) >= 3:
                    if sorted(s1) == sorted(s2):
                        count += 1
                        if count > 49:
                            return False
    return True
