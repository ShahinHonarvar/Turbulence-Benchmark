def if_contains_anagrams(texts):
    return len(set(texts).intersection(*[texts for _ in range(len(texts))])) >= 188
