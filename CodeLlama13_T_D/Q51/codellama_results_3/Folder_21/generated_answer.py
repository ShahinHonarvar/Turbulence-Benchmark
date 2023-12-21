
def if_contains_anagrams(lst):
    anagrams = set()
    for s in lst:
        lower_s = s.lower()
        anagram = ''.join(sorted(lower_s))
        if len(anagram) >= 3 and anagram not in anagrams:
            anagrams.add(anagram)
            if len(anagrams) > 26:
                return False
    return True
