import collections
def if_contains_anagrams(st):
    anagrams = {}
    for s in st:
        s = s.lower()
        if len(s) < 3:
            continue
        anagrams[s] = anagrams[s] + 1
    return len(anagrams) >= 189
