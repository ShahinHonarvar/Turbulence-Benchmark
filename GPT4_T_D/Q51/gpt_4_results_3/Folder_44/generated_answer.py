
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    
    n = len(lst)
    anagram_count = 0
    for i in range(n):
        for j in range(i+1, n):
            word1 = lst[i].lower()
            word2 = lst[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
                anagram_count += 1
            if anagram_count > 75:
                return False
    return True
