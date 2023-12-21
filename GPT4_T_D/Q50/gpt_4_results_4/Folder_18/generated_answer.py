
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    lst = [item.lower() for item in lst if len(item) >= 3]
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagrams_count += 1
            if anagrams_count >= 106:
                return True
    return False
