
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) >= 3:
            anagram = "".join(sorted(s.lower()))
            if anagram not in anagrams:
                anagrams.add(anagram)
                if len(anagrams) == 49:
                    return True
    return False
