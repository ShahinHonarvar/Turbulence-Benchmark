def if_contains_anagrams(texts):
    return bool(set(texts).intersection(set(map(str.lower, texts))).intersection(set(texts).intersection(set(map(str.lower, texts)))))
