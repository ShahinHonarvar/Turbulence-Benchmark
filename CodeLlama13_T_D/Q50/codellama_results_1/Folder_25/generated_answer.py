
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        anagrams.extend([x for x in strings if len(x) >= 3 and sorted(s) == sorted(x)])
    return len(anagrams) >= 14
