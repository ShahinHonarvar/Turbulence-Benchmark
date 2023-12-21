
def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        s = s.lower().replace(" ","")
        if len(s) >= 3 and s not in anagrams:
            anagrams.add(s)
    return len(anagrams) <= 73
