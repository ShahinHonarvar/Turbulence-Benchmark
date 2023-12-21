
from collections import Counter

def if_contains_anagrams(strings):
    word_groups = {}

    for word in strings:
        key = "".join(sorted(word.lower()))
        if key in word_groups:
            word_groups[key].append(word)
        else:
            word_groups[key] = [word]

    pairs = 0

    for words in word_groups.values():
        if len(words[0]) >= 3:
            counts = Counter(words)
            for count in counts.values():
                pairs += count *(count - 1) // 2

    return pairs >= 81
