
from collections import Counter

def if_contains_anagrams(str_list):
    def are_anagrams(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    anagram_pairs_count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and are_anagrams(str_list[i], str_list[j]):
                anagram_pairs_count += 1
                if anagram_pairs_count > 89:
                    return False
    return True
