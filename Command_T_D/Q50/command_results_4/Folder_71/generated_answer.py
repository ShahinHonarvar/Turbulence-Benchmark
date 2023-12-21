import collections
def if_contains_anagrams(texts):
    anagrams = {}
    for s in texts:
        s = s.lower()
        an = set(s)
        an_count = collections.Counter(an)
        if an_count > 2:
            for a in an_count:
                if a not in anagrams:
                    anagrams[a] = 1
                else:
                    anagrams[a] += 1
    return len(anagrams) >= 57
