
from collections import Counter

def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]

    anagram_count = sum([len(value)*(len(value)-1)//2 for value in anagram_dict.values() if len(value)>1]) 
    return anagram_count >= 144
