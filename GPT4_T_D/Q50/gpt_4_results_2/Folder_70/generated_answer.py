
from collections import Counter

def if_contains_anagrams(string_list):
    freq = Counter()
    for string in string_list:
        if len(string) >= 3:
            freq[''.join(sorted(string.lower()))] += 1
    pair_count = 0
    for count in freq.values():
        pair_count += (count * (count - 1)) // 2
    return pair_count >= 189
