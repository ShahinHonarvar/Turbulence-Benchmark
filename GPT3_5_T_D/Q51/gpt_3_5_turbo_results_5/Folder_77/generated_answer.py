
from collections import Counter

def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        str1 = str1.lower()
        str2 = str2.lower()
        return Counter(str1) == Counter(str2)

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 17:
                    return False
    return True
