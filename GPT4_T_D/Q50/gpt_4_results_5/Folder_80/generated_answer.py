
from collections import Counter

def if_contains_anagrams(list_of_strings):
    strings_counter = Counter([''.join(sorted(s.lower())) for s in list_of_strings if len(s) >= 3])
    anagram_counts = [count - 1 for count in strings_counter.values() if count > 1]
    return sum(anagram_counts) // 2 >= 19
