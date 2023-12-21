
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(word.lower())) for word in str_list if len(word) >= 3]
    word_counter = Counter(str_list)

    anagram_pair_count = 0
    for count in word_counter.values():
        anagram_pair_count += count * (count-1) // 2

    return anagram_pair_count >= 67
