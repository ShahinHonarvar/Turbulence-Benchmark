import collections
def if_contains_anagrams(texts):
    return len(list(filter(lambda x: x[0] == x[1], collections.Counter(x.lower() for x in texts).items()))) >= 25
