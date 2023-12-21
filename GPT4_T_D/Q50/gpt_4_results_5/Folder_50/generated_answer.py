
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)

    for string in string_list:
        if len(string) >= 3:
            sorted_string = "".join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    
    anagram_pairs_count = sum([len(value_list)*(len(value_list)-1)//2 for value_list in anagram_dict.values()])

    return anagram_pairs_count >= 20
