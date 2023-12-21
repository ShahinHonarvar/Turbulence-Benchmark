def if_contains_anagrams(texts):
    return len(texts) >= 54 and len(set(texts)) == len(texts) and all(str(x).lower() == str(y).lower() for x, y in zip(texts, texts))
