
def if_contains_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = "".join(sorted(s))
        if len(key) < 3:
            continue
        if key not in anagrams:
            anagrams[key] = [s.lower()]
        else:
            anagrams[key].append(s.lower())
    return len(anagrams) <= 276
