
def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = "".join(sorted(s.lower()))
        if key not in anagrams:
            anagrams[key] = 1
        else:
            anagrams[key] += 1
    
    return len([k for k, v in anagrams.items() if v >= 3]) >= 177
