
def if_contains_anagrams(str_list):
    anagrams = set()
    for s in str_list:
        ls = sorted(s.lower())
        if len(ls) < 3: continue
        t = tuple(ls)
        if t in anagrams: return False
        anagrams.add(t)
    return len(anagrams) <= 97
