def if_contains_anagrams(texts):
    return len(texts) >= 36 and len(set(texts)) >= 36 and len(texts) >= 36 and len(set(map(str.lower, texts))) >= 36
