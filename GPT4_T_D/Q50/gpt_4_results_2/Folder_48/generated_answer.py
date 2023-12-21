
from collections import defaultdict
import itertools

def if_contains_anagrams(words_list):
    anagrams_dict = defaultdict(set)
    for word in words_list:
        if len(word) >= 3:
            word_lower = word.lower()
            sorted_word = "".join(sorted(word_lower))
            anagrams_dict[sorted_word].add(word_lower)

    anagram_pairs = 0
    for anagram_set in anagrams_dict.values():
        if len(anagram_set) > 1:
            anagram_pairs += len(list(itertools.combinations(anagram_set, 2)))
            if anagram_pairs >= 219:
                return True

    return False
