
def if_contains_anagrams(lst):
    anagrams = []
    for s in lst:
        if len(s) >= 3:
            comparable_s = sorted(s.lower())
            for x in lst:
                if sorted(x.lower()) == comparable_s and s != x:
                    if (s, x) not in anagrams and (x, s) not in anagrams:
                        anagrams.append((s, x))
    if len(anagrams) >= 43:
        return True
    else:
        return False
