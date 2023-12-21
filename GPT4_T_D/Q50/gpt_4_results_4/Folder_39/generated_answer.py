
from collections import Counter

def if_contains_anagrams(str_list):
    anagram_dict = {}
    
    for string in str_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]

    anagram_pairs = [v for v in anagram_dict.values() if len(v) >= 2]
    
    pair_count = sum([len(list(zip(*[iter(v)]*2))) for v in anagram_pairs])
    
    return pair_count >= 54
