
from collections import Counter

def if_contains_anagrams(lst):
    counter_dict = Counter()
    for string in lst:
        if (string := string.lower()) and len(string) > 2:
            counter_dict[''.join(sorted(string))] += 1
    anagram_pairs = sum((count * (count - 1)) // 2 for count in counter_dict.values())
    return anagram_pairs >= 314
