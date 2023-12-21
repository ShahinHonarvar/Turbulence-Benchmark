
from collections import Counter

def if_contains_anagrams(lst_str):
    str_counter = [Counter(sorted(s.lower())) for s in lst_str if len(s) >= 3]
    count = 0
    for index, str1 in enumerate(str_counter[:-1]):
        for str2 in str_counter[index + 1:]:
            if str1 == str2:
                count += 1
                if count > 392:
                    return False
    return True
