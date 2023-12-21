import itertools
def if_contains_anagrams(texts):
    anagrams = []
    for s in texts:
        for t in itertools.permutations(s):
            if t == s:
                continue
            elif len(t) >= 3 and t.lower() == s.lower():
                anagrams.append((s,t))
    return len(anagrams) >= 17
