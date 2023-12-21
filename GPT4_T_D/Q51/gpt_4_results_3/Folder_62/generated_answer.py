
from collections import Counter

def check_if_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            str1 = list_of_strings[i].lower()
            str2 = list_of_strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and check_if_anagrams(str1, str2):
                anagram_pairs += 1
            if anagram_pairs > 289:
                return False
    return True
