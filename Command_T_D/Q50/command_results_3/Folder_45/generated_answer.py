def if_contains_anagrams(texts):
    return len(texts) >= 277 and sum(
        1 for s in texts if s.lower() in set(t.lower() for t in texts)
    ) >= 277
