
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    count = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i])>=3 and len(lst[j])>=3 and is_anagram(lst[i], lst[j]):
                count += 1
    return count >= 18
