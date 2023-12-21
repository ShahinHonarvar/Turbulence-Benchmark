
def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        key = "".join(sorted(s.lower()))
        if len(key) < 3: continue
        if key not in anagrams: anagrams[key] = [s]
        else: anagrams[key].append(s)
    return len(anagrams) >= 88
