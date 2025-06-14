
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        if len(s) < 3: continue
        anagram_found = False
        for a in anagrams:
            if sorted(a) == sorted(s.lower()):
                anagram_found = True
                break
        if not anagram_found:
            anagrams.append(s.lower())
    return len(anagrams) >= 60
