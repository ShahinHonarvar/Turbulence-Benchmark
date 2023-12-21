
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())

def if_contains_anagrams(str_list):
    str_list = [str for str in str_list if len(str) >= 3]
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 42:
                    return False
    return True
