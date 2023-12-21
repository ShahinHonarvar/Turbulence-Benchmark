
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        str1=str1.lower()
        str2=str2.lower()
        return sorted(str1)==sorted(str2)

    lst = [word for word in lst if len(word) >= 3]
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 42:
                    return False
    return True
