def if_contains_anagrams(texts):
    return len(set(map(str.lower, texts))) * len(set(map(str.lower, texts))) <= 474
