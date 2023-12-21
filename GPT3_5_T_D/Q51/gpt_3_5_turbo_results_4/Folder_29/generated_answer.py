
from collections import Counter

def if_contains_anagrams(list_of_strings):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            return False
        return Counter(s1) == Counter(s2)

    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if is_anagram(list_of_strings[i], list_of_strings[j]):
                count += 1
        if count > 318:
            return False

    return True
