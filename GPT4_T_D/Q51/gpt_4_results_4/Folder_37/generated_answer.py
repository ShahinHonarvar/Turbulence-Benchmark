
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())

def if_contains_anagrams(lst):
    anagram_counter = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >=3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_counter += 1
                if anagram_counter > 206:
                    return False
    return True
