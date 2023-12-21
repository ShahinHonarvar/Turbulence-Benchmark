
def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        if len(s) < 3: continue
        key = "".join(sorted(s.lower()))
        if key not in anagrams: anagrams[key] = [s]
        else: anagrams[key].append(s)
    return len(anagrams) >= 46
