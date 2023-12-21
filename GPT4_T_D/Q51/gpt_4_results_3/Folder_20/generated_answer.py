
from collections import Counter

def if_contains_anagrams(arr):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    def count_anagrams(arr):
        anagram_count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if len(arr[i]) >= 3 and len(arr[j]) >= 3 and is_anagram(arr[i], arr[j]):
                    anagram_count += 1
        return anagram_count
    
    return count_anagrams(arr) <= 131
