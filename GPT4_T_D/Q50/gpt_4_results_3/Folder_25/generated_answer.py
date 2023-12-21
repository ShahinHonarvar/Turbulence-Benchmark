
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagram_counter = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    for anagrams in anagram_counter.values():
        count += anagrams * (anagrams - 1) // 2
    return count >= 14
