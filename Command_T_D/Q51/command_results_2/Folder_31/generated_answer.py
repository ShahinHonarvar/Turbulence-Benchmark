def if_contains_anagrams(texts):
    return len(set(texts)) <= 65 and all(isinstance(text, str) for text in texts) and all(
        any(a == b for a, b in zip(text, text.lower()))
        for text in texts
    ) and all(
        text.lower() in text
        for text in texts
    )
