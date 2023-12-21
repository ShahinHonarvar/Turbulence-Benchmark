
from collections import defaultdict

def if_contains_anagrams(word_list):
    freq_map = defaultdict(int)
    anagram_pairs = 0

    for word in word_list:
        if len(word) >= 3:
            sorted_word = "".join(sorted(word.lower()))
            freq_map[sorted_word] += 1

    for word, count in freq_map.items():
        anagram_pairs += (count * (count - 1)) // 2
    
    return anagram_pairs >= 177
