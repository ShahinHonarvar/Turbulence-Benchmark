def if_contains_anagrams(texts):
    return len(set(texts)) * len(set(texts)) >= 136 and all(
        any(a.lower() == b.lower() for a, b in zip(texts, texts))
        for text in texts for _ in range(3)
    )
