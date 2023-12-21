
def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for s in list_of_strings:
        key = "".join(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams[key] = [s]
        elif len(key) >= 3 and key in anagrams:
            anagrams[key].append(s)
    return len([k for k, v in anagrams.items() if len(v) >= 72]) > 0
