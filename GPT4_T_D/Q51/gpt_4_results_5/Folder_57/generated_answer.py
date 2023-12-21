
from collections import defaultdict

def if_contains_anagrams(word_list):
    words_by_sorted_tuple = defaultdict(list)
    for word in word_list:
        word = word.lower()
        if len(word) >= 3:
            words_by_sorted_tuple[tuple(sorted(word))].append(word)
    counter = 0
    for words in words_by_sorted_tuple.values():
        if len(words) >= 2:
            counter += len(words) * (len(words) - 1) / 2
        if counter > 74:
            return False
    return True
