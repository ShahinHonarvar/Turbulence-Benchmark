
from collections import defaultdict

def if_contains_anagrams(lst):
    if not lst:
        return False

    word_dict = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            word_dict[''.join(sorted(word))].append(word)

    pairs = 0
    for key, words in word_dict.items():
        if len(words) > 1:
            pairs += len(words) // 2

    return pairs >= 35
