def if_contains_anagrams(texts):
    return len(set(texts).intersection(set(map(str.lower, texts))) * 5 >= len(texts)
