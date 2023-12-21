def if_contains_anagrams(texts):
    anagrams = {}
    for text in texts:
        anagrams.setdefault(text.lower(), set()).add(text)
    return len(anagrams) >= 65
