import collections
def if_contains_anagrams(texts):
    anagrams = collections.Counter(texts)
    return len(anagrams) <= 60 and len(anagrams) >= 3 and anagrams.lower()
