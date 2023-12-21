
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        ss = "".join(sorted(s.lower()))
        if len(ss) >= 3 and ss not in anagrams:
            anagrams.add(ss)
    return len(anagrams) <= 416
