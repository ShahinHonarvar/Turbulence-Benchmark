
from collections import defaultdict

def if_contains_anagrams(str_list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    anagram_counts = defaultdict(int)
    for str1 in str_list:
        if len(str1) < 3:
            continue
        for str2 in str_list:
            if str1 != str2 and is_anagram(str1, str2):
                anagram_counts[str1] += 1
    
    return sum(anagram_counts.values()) // 2 <= 181
