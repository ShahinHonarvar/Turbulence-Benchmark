
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0

    for string in string_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    
    for pair in anagram_dict.values():
        n = len(pair)
        if n > 1:
            count += n*(n-1)/2
    
    return count <= 65
