
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    
    # create a dictionary where keys - sorted strings, values - original strings
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    
    anagram_pairs = 0
    for values in anagram_dict.values():
        anagram_pairs += len(values) * (len(values) - 1) // 2
    
    return anagram_pairs >= 58
