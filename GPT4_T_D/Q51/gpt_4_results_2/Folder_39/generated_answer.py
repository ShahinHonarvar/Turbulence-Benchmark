
from collections import Counter

def if_contains_anagrams(str_list):
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    
    lower_str_list = [s.lower() for s in str_list if len(s) >= 3]
    anagram_count = 0
    
    for i in range(len(lower_str_list)):
        for j in range(i+1, len(lower_str_list)):
            if is_anagram(lower_str_list[i], lower_str_list[j]):
                anagram_count += 1
                if anagram_count > 257:
                    return False
    
    return True
