
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        for i, t in enumerate(s[3:]):
            if t in anagrams:
                return True
            else:
                anagrams.append(t)
    return False
