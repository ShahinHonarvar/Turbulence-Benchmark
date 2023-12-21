
from collections import defaultdict

def if_contains_anagrams(lst):
    word_groups = defaultdict(list)
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_groups[sorted_word].append(word)
    
    anagram_pairs = 0
    for word_group in word_groups.values():
        anagram_pairs += len(word_group) * (len(word_group) - 1) // 2

    return anagram_pairs >= 49
