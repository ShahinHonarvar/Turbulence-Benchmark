
from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

def if_contains_anagrams(str_list):
    count = 0
    checked = []
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) > 2 and len(str_list[j]) > 2 and str_list[i].lower() not in checked:
                if is_anagram(str_list[i].lower(), str_list[j].lower()):
                    count += 1
                    checked.append(str_list[i].lower())
    return count <= 43
