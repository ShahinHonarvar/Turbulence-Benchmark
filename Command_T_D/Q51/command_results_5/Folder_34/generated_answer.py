import collections
def if_contains_anagrams(s):
    return sum(1 for x,y in collections.Counter(s).items() if (x,y) in [(a,b) for a,b in zip(x.lower(), y.lower()) if len(set(a))==len(set(b))]) <= 401
