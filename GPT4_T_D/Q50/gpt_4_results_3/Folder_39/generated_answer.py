
from collections import Counter

def if_contains_anagrams(lst):
    sorted_word_list = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    frequencies = Counter(sorted_word_list)
    pairs = 0
    for value in frequencies.values():
        pairs += value // 2
    return pairs >= 54
