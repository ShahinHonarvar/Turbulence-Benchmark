
from collections import defaultdict

def if_contains_anagrams(words):
    word_groups = defaultdict(list)
    
    for word in words:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_groups[sorted_word].append(word)
    
    anagram_pairs = 0
    for words in word_groups.values():
        anagram_pairs += len(words) * (len(words) - 1) // 2

    return anagram_pairs <= 34
