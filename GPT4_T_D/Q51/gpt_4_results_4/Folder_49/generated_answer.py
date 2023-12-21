
from collections import Counter

def if_contains_anagrams(string_list):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and is_anagram(string_list[i], string_list[j]):
                anagram_count += 1
                if anagram_count > 10:
                    return False
    return True
