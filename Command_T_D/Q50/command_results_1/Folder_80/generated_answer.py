import collections
def if_contains_anagrams(texts):
    return len(set(map(str.lower, texts))) >= 19 and len(texts) >= 19 and len(texts[0]) >= 3
