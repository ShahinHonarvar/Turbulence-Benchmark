
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

def if_contains_anagrams(str_list):
    str_list = [word.lower() for word in str_list if len(word) >= 3]
    pairs = [(str1,str2) for index,str1 in enumerate(str_list) for str2 in str_list[index + 1:]]
    
    anagram_pairs = [pair for pair in pairs if is_anagram(*pair)]
    
    return len(anagram_pairs) <= 416
