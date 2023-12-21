
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

def if_contains_anagrams(list_of_strings):
    anagram_counter = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if (len(list_of_strings[i]) >= 3) and (len(list_of_strings[j]) >= 3):
                if is_anagram(list_of_strings[i].lower(), list_of_strings[j].lower()):
                    anagram_counter += 1
            if anagram_counter > 73:
                return False
    return True
