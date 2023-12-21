
from collections import Counter

def if_contains_anagrams(str_list):
    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and is_anagram(str_list[i].lower(), str_list[j].lower()):
                anagram_pairs += 1
                if anagram_pairs > 94:
                    return False
    return True
