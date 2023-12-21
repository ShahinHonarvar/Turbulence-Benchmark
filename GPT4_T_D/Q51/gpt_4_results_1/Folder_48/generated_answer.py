
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(int)
    
    # Sort word and add to dictionary
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_dict[sorted_word] += 1

    # Count pairs of anagrams
    anagram_pairs = 0
    for word_count in word_dict.values():
        anagram_pairs += (word_count * (word_count - 1)) // 2

    return anagram_pairs <= 277
