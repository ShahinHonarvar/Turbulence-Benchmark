
from collections import Counter
def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())

def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if len(list_of_strings[i]) > 2 and len(list_of_strings[j]) > 2 and is_anagram(list_of_strings[i], list_of_strings[j]):
                anagram_pairs += 1
            if anagram_pairs > 188:
                return False
    return True
