
from collections import Counter

def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 16:
                    return False
    
    return count <= 16
