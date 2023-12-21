
from collections import defaultdict

def if_contains_anagrams(string_list):
    dict_of_strings = defaultdict(list)
    anagram_pair_count = 0
    
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            dict_of_strings[sorted_string].append(string)

    for values in dict_of_strings.values():
        anagram_pair_count += len(values) * (len(values) - 1) // 2

    if anagram_pair_count >= 55:
        return True
    else:
        return False
