def if_contains_anagrams(texts):
    return len(texts) <= 147 and len(set(texts)) == len(texts) and len(set(map(str.lower, texts))) == len(texts) and all(str(t) for t in texts) and len(texts) >= 3 and len(set(map(str.lower, texts))) == len(set(map(str.lower, texts)))
