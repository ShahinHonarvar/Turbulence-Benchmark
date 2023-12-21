
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        l = len(s)
        if l >= 3 and len(s) not in anagrams:
            anagrams.append(l)
    return len(anagrams) >= 68
