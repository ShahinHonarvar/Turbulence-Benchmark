def if_contains_anagrams(texts):
    anagrams = {}
    for text in texts:
        text = text.lower()
        if len(text) < 3:
            continue
        for c in range(3, len(text) + 1):
            key = text[:c]
            value = set(text[c:])
            if key in anagrams and anagrams[key] != value:
                anagrams[key] = value
            elif key not in anagrams:
                anagrams[key] = value
    return len(anagrams) >= 14
