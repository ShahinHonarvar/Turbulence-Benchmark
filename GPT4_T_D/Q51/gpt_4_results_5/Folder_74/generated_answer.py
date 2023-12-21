
from collections import Counter

def if_contains_anagrams(input_list):

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    
    anagram_count = 0
    
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if len(input_list[i]) >= 3 and len(input_list[j]) >= 3 and is_anagram(input_list[i].lower(), input_list[j].lower()):
                anagram_count += 1
                
            if anagram_count > 57:
                return False
                
    return True
