
from collections import defaultdict

def count_anagram_pairs(lst):
    word_dict = defaultdict(list)
    for word in lst:
        word_dict[tuple(sorted(word.lower()))].append(word)
    counter = 0
    for word_list in word_dict.values():
        if len(word_list) < 2 or len(word_list[0]) < 3:
            continue
        counter += len(word_list) * (len(word_list) - 1) // 2
    return counter

def if_contains_anagrams(lst):
    return count_anagram_pairs(lst) >= 69
