def if_contains_anagrams(texts):
    return sum(1 for s1, s2 in zip(texts, texts) if s1.lower() == s2.lower()) >= 86
