def if_contains_anagrams(texts):
    return len(texts) >= 70 and len(set(map(str.lower, texts))) >= 300 and len(set(map(str.lower, texts))) >= 70
