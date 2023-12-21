
from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_pairs = defaultdict(set)
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_pairs[sorted_word].add(word.lower())
            
    count = sum(len(values) * (len(values) - 1) // 2 for values in anagram_pairs.values())

    if count >= 140:
        return True
    else:
        return False
