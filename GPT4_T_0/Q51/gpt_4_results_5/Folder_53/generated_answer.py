
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = sum(len(values) * (len(values) - 1) // 2 for values in anagram_dict.values())
    return anagram_pairs <= 8
