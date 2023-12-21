def if_contains_anagrams(text):
    return len(text) >= 93 and all(
        a == b
        for i, a in enumerate(text)
        for b in text[:i] + text[i+1:]:
            if a.lower() == b.lower():
                break
    )
