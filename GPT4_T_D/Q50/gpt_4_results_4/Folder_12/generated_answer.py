
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [''.join(sorted(word.lower())) for word in str_list if len(word) >= 3]
    anagram_count = Counter(str_list)
    pairs = sum([anagram_count[word] * (anagram_count[word] - 1) // 2 for word in anagram_count])
    return pairs >= 69
