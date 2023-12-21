
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    pair_count = 0
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_dict:
                pair_count += len(anagram_dict[sorted_string])
                if pair_count > 47:
                    return False
            anagram_dict[sorted_string].append(string)
    return True
