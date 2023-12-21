
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    lst = [s.lower() for s in lst if len(s)>=3]
    anagram_count = 0

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_count+= 1
            if anagram_count >= 155:
                return True
    return False
