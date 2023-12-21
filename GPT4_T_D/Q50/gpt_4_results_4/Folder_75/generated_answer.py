
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

def if_contains_anagrams(str_list):
    count = 0
    str_list = [x.lower() for x in str_list if len(x) >= 3]
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                count += 1
                if count >= 70:
                    return True
    return False
