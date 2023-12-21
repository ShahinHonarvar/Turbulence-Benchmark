
def if_contains_anagrams(string_list):
    anagrams = set()
    for s in string_list:
        t = tuple(sorted(s.lower()))
        if len(t) >= 3 and t not in anagrams:
            anagrams.add(t)
            if len(anagrams) >= 58:
                return True
    return False
