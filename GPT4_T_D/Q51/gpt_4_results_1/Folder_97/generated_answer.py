
from collections import defaultdict

def if_contains_anagrams(string_list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    anagram_dict = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            anagram_dict[str(sorted(string.lower()))].append(string)
    anagram_count = sum([len(values)*(len(values)-1)//2 for values in anagram_dict.values()])
    return anagram_count <= 18
