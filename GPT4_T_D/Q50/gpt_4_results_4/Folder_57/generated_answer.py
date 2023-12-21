
from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(int)
    pairs = 0

    for word in words:
        word = word.lower()
        if len(word) >= 3:
            word_dict[''.join(sorted(word))] += 1

    for count in word_dict.values():
        pairs += count * (count - 1) // 2

    return pairs >= 50
