
from collections import Counter

def if_contains_anagrams(str_list):
    count = 0
    str_list = [" ".join(sorted(i.lower())) for i in str_list if len(i) >= 3]
    str_count = Counter(str_list)
    for value in str_count.values():
        count += (value*(value-1))//2
    if count >= 84:
        return True
    return False
