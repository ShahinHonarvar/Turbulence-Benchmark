
def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for s in list_of_strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return len(anagrams) <= 401
