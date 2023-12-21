
from collections import defaultdict

def if_contains_anagrams(lst):
    freq_dict = defaultdict(int)

    def count_anagram_pairs(freq_dict):
        return sum(freq * (freq-1) // 2 for freq in freq_dict.values())

    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3 and word.isalpha():
            freq_dict[word] += 1

    return count_anagram_pairs(freq_dict) <= 206
