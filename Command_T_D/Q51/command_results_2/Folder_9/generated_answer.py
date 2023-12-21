import collections
def if_contains_anagrams(texts):
    return len(set(anagrams(texts))) <= 475
def anagrams(texts):
    seen = set()
    return [w for w in texts if len(w) >= 3 and w not in seen and seen.add(w.lower())]
