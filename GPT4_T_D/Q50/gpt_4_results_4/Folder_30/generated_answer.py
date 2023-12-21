
from collections import Counter

def if_contains_anagrams(lst_str):
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    
    pairs_counter = 0
    anagrams = []
    for i in range(len(lst_str)):
        for j in range(i+1, len(lst_str)):
            if len(lst_str[i])>=3 and len(lst_str[j])>=3 and is_anagram(lst_str[i].lower(), lst_str[j].lower()):
                pairs_counter += 1
                if pairs_counter == 78:
                    return True
    return False
