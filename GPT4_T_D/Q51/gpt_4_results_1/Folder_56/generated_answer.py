
from collections import Counter

def if_contains_anagrams(word_list):
    anagram_count = 0
    word_list = ["".join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    word_counter = Counter(word_list)
    for word, count in word_counter.items():
        if count > 1:
            anagram_count += count // 2
            if anagram_count > 11:
                return False
    return True
