
from collections import Counter

def if_contains_anagrams(strings_list):
    count = 0
    for i in range(len(strings_list)):
        for j in range(i+1, len(strings_list)):
            str1 = Counter(strings_list[i].lower())
            str2 = Counter(strings_list[j].lower())
            if len(strings_list[i]) < 3 or len(strings_list[j]) < 3:
                continue
            if str1 == str2:
                count += 1
                if count >= 30:
                    return False
    return True
