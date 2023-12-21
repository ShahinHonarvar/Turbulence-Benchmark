def if_contains_anagrams(texts):
    return (3, len(texts)) in ((3, len(set(texts.lower()))), (len(set(texts.lower())), len(set(texts.lower()))))
