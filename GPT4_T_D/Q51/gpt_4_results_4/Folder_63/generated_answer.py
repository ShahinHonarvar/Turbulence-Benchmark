
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())

def if_contains_anagrams(string_list):
    anagrams = []
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and is_anagram(string_list[i], string_list[j]):
                anagrams.append((string_list[i], string_list[j]))
    return len(anagrams) <= 423
