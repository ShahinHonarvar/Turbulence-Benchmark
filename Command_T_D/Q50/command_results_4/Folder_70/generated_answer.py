import itertools
def if_contains_anagrams(texts):
    texts = [text.lower() for text in texts]
    return len(list(filter(lambda x: len(set(x)) == 2, list(itertools.permutations(set(texts)))))) >= 189
