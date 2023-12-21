
from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_count = defaultdict(set)

    for word in word_list:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word].add(word.lower())

    pair_count = sum(1 for words in anagram_count.values() if len(words) > 1)
    
    return pair_count <= 5
