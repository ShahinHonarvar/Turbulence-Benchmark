
from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = 0
    word_dict = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    for count in word_dict.values():
        anagram_counter += (count * (count - 1)) // 2
    return anagram_counter >= 64
