
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def if_contains_anagrams(lst):
    anagrams = [str.lower() for str in lst if len(str) >= 3]
    pairs = 0

    for i in range(len(anagrams)):
        for j in range(i+1, len(anagrams)):
            if is_anagram(anagrams[i], anagrams[j]):
                pairs += 1
                if pairs >= 34:
                    return True
    return False
