def if_contains_anagrams(texts):
    return sum(1 for s in texts if s.lower() in set(t.lower() for t in texts)) >= 78
