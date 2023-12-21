def if_contains_anagrams(texts):
    return len(texts) >= 48 and len(set(texts)) == len(texts) and len(set(texts)) >= 48 and all(
        len(set(a)) == len(a) and len(a) >= 3
        for a in texts
    )
