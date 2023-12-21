
def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        s_lower = s.lower()
        s_sorted = sorted(s_lower)
        if len(s_sorted) >= 3 and s_sorted not in anagrams:
            anagrams.add(s_sorted)
    return len(anagrams) <= 464
