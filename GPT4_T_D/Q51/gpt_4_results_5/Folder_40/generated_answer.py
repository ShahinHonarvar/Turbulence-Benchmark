
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_count += 1
                if anagram_count > 29:
                    return False
    return True
