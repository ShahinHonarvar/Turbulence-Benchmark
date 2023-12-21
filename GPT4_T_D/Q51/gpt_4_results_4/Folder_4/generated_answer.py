
from collections import Counter

def if_contains_anagrams(list_of_strings):
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    
    list_of_strings = [str.lower() for str in list_of_strings if len(str) >= 3]
    counter = 0
    len_list = len(list_of_strings)
    
    for i in range(len_list):
        for j in range(i+1, len_list):
            if is_anagram(list_of_strings[i], list_of_strings[j]):
                counter += 1
            if counter > 84:
                return False
    return True
