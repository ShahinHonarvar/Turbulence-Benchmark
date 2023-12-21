import collections
def if_contains_anagrams(texts):
    texts = sorted(set(texts))
    dct = collections.defaultdict(list)
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            if texts[i] == texts[j].lower():
                dct[texts[i]].append(texts[j])
    return len(dct) > 26
