
from collections import Counter

def if_contains_anagrams(str_list):
    anagram_counter = Counter(''.join(sorted(word.lower())) for word in str_list if len(word) >= 3)
    return sum(1 for count in anagram_counter.values() if count > 1) >= 22
