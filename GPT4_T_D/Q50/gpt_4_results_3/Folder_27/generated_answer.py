
from collections import defaultdict

def if_contains_anagrams(lst):
    hash_table = defaultdict(list)
    pairs = []

    for word in lst:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            hash_table[sorted_word].append(word)

    for words in hash_table.values():
        if len(words) >= 2:
            pairs.extend(words)

    return len(pairs) >= 86
