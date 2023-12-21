def if_contains_anagrams(texts):
    return sum(x.lower() == y.lower() for x, y in zip(texts, texts)) >= 15
