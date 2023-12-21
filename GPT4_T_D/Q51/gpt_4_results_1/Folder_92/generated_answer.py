
from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s].append(s)

    counter = 0
    for key, value in anagram_dict.items():
        if len(value)>1:
            counter += len(value) * (len(value) - 1) // 2
            
    return counter <= 34
