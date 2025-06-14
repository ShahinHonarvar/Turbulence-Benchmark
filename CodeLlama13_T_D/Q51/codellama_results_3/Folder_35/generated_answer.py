
def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams.add(key)
            if len(anagrams) > 210:
                return False
    return True
