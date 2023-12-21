import collections
def if_contains_anagrams(texts):
    anagrams = collections.defaultdict(set)
    for s in texts:
        letters = set(s.lower())
        for k in letters:
            anagrams[k].add(s)
    return len(anagrams) <= 181
