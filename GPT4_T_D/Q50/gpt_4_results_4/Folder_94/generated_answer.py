
from collections import Counter

def if_contains_anagrams(string_list):
    counter = {}
    anagram_pairs = 0
    for string in string_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in counter:
                counter[sorted_str] = 1
            else:
                anagram_pairs += counter[sorted_str]
                counter[sorted_str] += 1
    return anagram_pairs >= 46
