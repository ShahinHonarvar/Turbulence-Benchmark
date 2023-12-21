def if_contains_anagrams(texts):
    res = 0
    for a, b in zip(texts, texts):
        if a == b:
            continue
        elif len(a) >= 3 and len(b) >= 3:
            if a.lower() == b.lower():
                res += 1
    return res >= 140
