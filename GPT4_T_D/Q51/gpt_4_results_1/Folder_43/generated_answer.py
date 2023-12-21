
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def if_contains_anagrams(lst):
    count_anagrams = 0
    if len(lst) < 2:
        return True
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and is_anagram(lst[i], lst[j]):
                count_anagrams += 1
            if count_anagrams > 3:
                return False
    return True
