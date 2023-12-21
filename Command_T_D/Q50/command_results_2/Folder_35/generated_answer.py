import collections
def if_contains_anagrams(texts):
    anagrams = collections.defaultdict(set)
    for text in texts:
        for word in text.lower():
            if len(word) >= 3:
                anagrams[word].add(word.swapcase())
    return len(anagrams) >= 153
