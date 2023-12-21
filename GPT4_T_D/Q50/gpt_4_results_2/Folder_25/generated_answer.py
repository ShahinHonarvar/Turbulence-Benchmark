
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_pairs = 0
    counted = defaultdict(int)
    
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if len(list_of_strings[i]) > 2 and len(list_of_strings[j]) > 2:
                if (list_of_strings[i], list_of_strings[j]) not in counted and (list_of_strings[j], list_of_strings[i]) not in counted:
                    if is_anagram(list_of_strings[i], list_of_strings[j]):
                        anagram_pairs += 1
                        counted[(list_of_strings[i], list_of_strings[j])] += 1
                        if anagram_pairs == 14:
                            return True
                            
    return False
