
from collections import Counter

def if_contains_anagrams(str_list):
    count = 0
    for i in range(len(str_list)-1):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if Counter(str_list[i].lower()) == Counter(str_list[j].lower()):
                    count += 1
                    if count > 86:
                        return False
    return True
