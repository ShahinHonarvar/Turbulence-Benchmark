def if_contains_anagrams(texts):
    texts = set(texts)
    texts = sorted(texts)
    texts = {elt: str(i) for i, elt in enumerate(texts)}
    for i in range(len(texts) - 2):
        for j in range(i + 1, len(texts)):
            if texts[i] == texts[j]: continue
            if sorted(texts[i]) == sorted(texts[j]):
                return True
    return False
