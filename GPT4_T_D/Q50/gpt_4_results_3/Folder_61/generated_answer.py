
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())

def if_contains_anagrams(words):
    pair_count = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and is_anagram(words[i], words[j]):
                pair_count += 1
                if pair_count >= 8:
                    return True
    return False
