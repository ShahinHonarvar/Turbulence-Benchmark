
from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(int)
    pairs = 0

    for word in words:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            word_dict[word] += 1

    for count in word_dict.values():
        pairs += count * (count - 1) / 2

    if pairs <= 66:
        return True
    else:
        return False
