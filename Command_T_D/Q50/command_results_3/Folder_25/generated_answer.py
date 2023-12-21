import collections
def if_contains_anagrams(s):
    return len(list(filter(
        lambda x: len(x)>=3 and collections.Counter(x.lower())==collections.Counter(y.lower()) for x,y in zip(s,s)
    )))>=14
