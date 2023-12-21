
from collections import Counter

def if_contains_anagrams(words):
    sorted_words = []
    for word in words:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            sorted_words.append(sorted_word)

    count = Counter(sorted_words)
    pairs = sum(val // 2 for val in count.values())
    return pairs >= 24
