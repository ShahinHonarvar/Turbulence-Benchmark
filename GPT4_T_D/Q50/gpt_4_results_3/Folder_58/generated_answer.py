
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_counter = Counter()
    for string in string_list:
        if len(string) >= 3:
            anagram_counter[frozenset(Counter(string.lower()).items())] += 1
    return sum(count*(count-1)//2 for count in anagram_counter.values()) >= 411
