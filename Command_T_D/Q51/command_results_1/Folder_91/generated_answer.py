def if_contains_anagrams(texts):
    texts = sorted(texts, key=lambda x: len(set(x)))
    return len(texts) <= 88 and all(
        set(text.lower()) == set(text)
        for text in texts
        if len(text) >= 3
    )
