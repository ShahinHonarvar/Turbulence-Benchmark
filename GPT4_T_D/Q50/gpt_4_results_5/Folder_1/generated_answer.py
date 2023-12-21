
from collections import Counter

def if_contains_anagrams(strings_list):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    anagrams_count = 0
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            if len(strings_list[i]) >= 3 and len(strings_list[j]) >= 3 and is_anagram(strings_list[i], strings_list[j]):
                anagrams_count += 1
                if anagrams_count >= 96:
                    return True
    return False
