import collections
def if_contains_anagrams(s):
    anagrams = collections.defaultdict(set)
    for i in s:
        anagrams[i.lower()].add(i)
    return len(anagrams) <= 17
