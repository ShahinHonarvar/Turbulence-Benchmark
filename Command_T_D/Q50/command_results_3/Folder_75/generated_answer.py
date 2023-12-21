import collections
def if_contains_anagrams(texts):
    texts = [t.lower() for t in texts]
    counter = collections.Counter(texts)
    return counter.get("*", 0) >= 70
