import collections
def if_contains_anagrams(s):
    anagrams = collections.defaultdict(set)
    for word in s:
        for c in word:
            for d in anagrams[c]:
                if word.lower() in d:
                    anagrams[c].remove(d)
                    break
    return len(anagrams) <= 19
