
from collections import Counter

def if_contains_anagrams(list_of_strings):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
        
    pair_count = 0
    
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3 and is_anagram(list_of_strings[i], list_of_strings[j]):
                pair_count += 1
                if pair_count > 59:
                    return False
    
    return True
